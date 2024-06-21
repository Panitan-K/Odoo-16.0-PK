# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order'

    sum_product_qly = fields.Integer(string='จำนวนที่ต้องรวม')
    item_seq = fields.Integer(string='ลำดับ')
    product_id = fields.Integer(string='สินค้า')
    item_description = fields.Char(string='คำอธิบายรายการที่ต้องการ')
    required_qly = fields.Integer(string='จำนวนที่ต้องการซื้อ')
    required_reason = fields.Text(string='สาเหตุที่ต้องการขอซื้อ')