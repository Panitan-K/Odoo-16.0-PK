# -*- coding: utf-8 -*-
import logging
from odoo import models, fields, api
_logger = logging.getLogger(__name__)

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order'


    #item_seq = fields.Integer(string='ลำดับ')
    #product_id = fields.Integer(string='สินค้า')
    #item_description = fields.Char(string='คำอธิบายรายการที่ต้องการ')
    #required_qty = fields.Integer(string='จำนวนที่ต้องการซื้อ')
    #required_reason = fields.Text(string='สาเหตุที่ต้องการขอซื้อ')
    employee_id = fields.Many2one('hr.employee', string='ผู้ขอซื้อ')

    sum_product_qty = fields.Float(string='จำนวนที่ต้องรวม', compute='_compute_sum_product_qty')

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