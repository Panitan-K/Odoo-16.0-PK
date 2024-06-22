# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order'


    item_seq = fields.Integer(string='ลำดับ')
    product_id = fields.Integer(string='สินค้า')
    item_description = fields.Char(string='คำอธิบายรายการที่ต้องการ')
    required_qly = fields.Integer(string='จำนวนที่ต้องการซื้อ')
    required_reason = fields.Text(string='สาเหตุที่ต้องการขอซื้อ')
    employee_id = fields.Many2one('hr.employee', string='ผู้ขอซื้อ')

    sum_product_qly = fields.Float(string='จำนวนที่ต้องรวม', compute='_compute_sum_product_qly')

    @api.depends('order_line.product_qty')
    def _compute_sum_product_qly(self):
        for order in self:
            order.sum_product_qly = sum(line.product_qty for line in order.order_line)