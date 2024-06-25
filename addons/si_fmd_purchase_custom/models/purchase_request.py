# -*- coding: utf-8 -*-
import logging
from odoo import models, fields, api
_logger = logging.getLogger(__name__)
from datetime import datetime
import pytz
class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    sum_product_qty = fields.Float(string='จำนวนที่ต้องรวม', compute='_compute_sum_product_qty')
    partner_id = fields.Many2one(
        'res.partner',
        string='Vendor',
        required=False,  # Ensure this is not required at the model level
        index=True,
        tracking=True
    )

    employee_id = fields.Many2one(
        'hr.employee',
        string='ผู้ขอซื้อ',
        required=True,  # Make employee_id required
        index=True,
        tracking=True
    )
    @api.depends('order_line.required_qty')
    def _compute_sum_product_qty(self):
        for order in self:
            order.sum_product_qty = sum(line.required_qty for line in order.order_line)

    def action_si_request_purchase_rm(self):
        # Collect specific attributes of the purchase order record
        attributes = {
            'display_name': self.display_name,
        }

        # Pass the attributes to the report context
        return self.env.ref('si_fmd_purchase_custom.report_purchase_request_attributes').report_action(self, data={
            'attributes': attributes
        })

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            order_type = vals.get('z_po_type', 'PR')
            #company_internal_code = self.env.user.company_id.x_company_internal_code
            company_internal_code = "XXXX"
            date = datetime.today()
            prefix = f"{order_type}-{company_internal_code}{date.strftime('%y%m%d')}"
            seq = self.env['ir.sequence'].next_by_code('purchase.order')
            vals['name'] = f"{prefix}{seq}"
        return super(PurchaseOrder, self).create(vals)