# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
from datetime import datetime
import pytz  # Ensure pytz is imported if using timezone-aware datetime

_logger = logging.getLogger(__name__)


class BagType(models.Model):
    _inherit = 'purchase.order.line'

    protein_pct = fields.Float(string='โปรตีน (%)')
    tvbn_unit = fields.Float(string='TVBN')
    rm_weight_unit = fields.Float(string='นน. RM ที่ชั่งได้ (กก.)')
    number_of_sag = fields.Integer(string='จำนวนกระสอบ')
    sag_type_id = fields.Many2one('si.sag.type', string='ประเภทกระสอบ')
    qty_weight_computed = fields.Float(string='จำนวน (QTY)', compute='_compute_weight_qty', store=True)
    price_subtotal = fields.Float(string='มูลค่าสุทธิ', compute='_compute_price_subtotal', store=True)

    item_seq = fields.Integer(string='ลำดับ')
    item_description = fields.Char(string='คำอธิบายรายการที่ต้องการ')
    required_qty = fields.Integer(string='จำนวนที่ต้องการซื้อ')
    required_reason = fields.Text(string='สาเหตุที่ต้องการขอซื้อ')

    order_id = fields.Many2one('purchase.order', string='Order Reference')

    @api.depends('rm_weight_unit', 'number_of_sag', 'sag_type_id')
    def _compute_weight_qty(self):
        for line in self:
            if line.sag_type_id:
                line.qty_weight_computed = line.rm_weight_unit - (line.number_of_sag * line.sag_type_id.weight)
                line.product_qty = line.rm_weight_unit - (line.number_of_sag * line.sag_type_id.weight)
            else:
                line.qty_weight_computed = line.rm_weight_unit
                line.product_qty = line.rm_weight_unit

    @api.depends('rm_weight_unit', 'number_of_sag', 'sag_type_id')
    def _compute_product_qty(self):
        for line in self:
            if line.sag_type_id:
                line.product_qty = line.rm_weight_unit - (line.number_of_sag * line.sag_type_id.weight)
            else:
                line.product_qty = line.rm_weight_unit

    @api.depends('price_unit', 'required_qty')
    def _compute_price_subtotal(self):
        for line in self:
            # Ensure that required_qty is not None or zero before multiplication
            if line.price_unit and line.required_qty:
                line.price_subtotal = line.price_unit * line.required_qty
            else:
                line.price_subtotal = 0.0  # Set to 0.0 if any value is missing





