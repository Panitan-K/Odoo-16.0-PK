# -*- coding: utf-8 -*-
import logging
from odoo import models, fields, api
_logger = logging.getLogger(__name__)
from datetime import datetime
import pytz
class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    #order_id = fields.Many2one('purchase.order', string='Order Reference')
    #price_unit = fields.Many2one('purchase.price_unit', string='Order Reference')
    #product_qty = fields.Many2one('purchase.product_qty', string='Order Reference')
    #product_uom = fields.Many2one('purchase.product_uom', string='Order Reference')
    #price_subtotal = fields.Many2one('purchase.product_uom', string='Order Reference')
    order_id = fields.Many2one('purchase.order', string='Order Reference')
    product_qty = fields.Many2one('purchase.order', string="ProductQTY")
    price_unit = fields.Many2one('purchase.order', string='Price Unit')
    taxes_id = fields.Many2one('purchase.order', string='Taxes')
    invoice_lines = fields.One2many('account.move.line', 'purchase_line_id', string="Bill Lines", readonly=True,
                                    copy=False)


    date_order = fields.Datetime(string='วันที่ขอซื้อ/จัดจ้าง')
    date_planned = fields.Datetime(string='วันที่ต้องการสินค้า')
    sum_product_qty = fields.Float(string='จำนวนที่ต้องรวม', compute='_compute_sum_product_qty')
    employee_id = fields.Many2one(
        'hr.employee',
        string='ผู้ขอซื้อ',
        required=True,  # Make employee_id required
        index=True,
        tracking=True
    )

    @api.model
    def Create_Request_Order(self):
        # Define the action you want to perform
        return {
            'type': 'ir.actions.act_window',
            'name': 'New Window Action',
            'res_model': 'purchase.order',
            'view_mode': 'tree,form',
            'target': 'new',
        }

    @api.depends_context('from_request_tree')
    def _compute_show_custom_fields(self):
        for record in self:
            record.show_custom_fields = self.env.context.get('from_request_tree', False)
    @api.depends('order_line.product_qty')
    def _compute_sum_product_qty(self):
        for order in self:
            order.sum_product_qty = sum(line.product_qty for line in order.order_line)

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
            vals['name'] = f"{prefix}{seq[1:]}"
        return super(PurchaseOrder, self).create(vals)