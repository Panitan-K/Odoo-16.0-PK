# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)


class BagType(models.Model):
    _inherit = 'purchase.order.line'

    protein_pct = fields.Float(string='โปรตีน (%)')
    tvbn_unit = fields.Float(string='TVBN')
    rm_weight_unit = fields.Float(string='นน. RM ที่ชั่งได้ (กก.)')
    number_of_sag = fields.Integer(string='จำนวนกระสอบ')
    sag_type_id = fields.Many2one('si.sag.type', string='ประเภทกระสอบ')
    qty_weight_computed = fields.Float(string='จำนวน (QTY)', compute='_compute_weight_qty', store=True)

    item_seq = fields.Integer(string='ลำดับ')
    item_description = fields.Char(string='คำอธิบายรายการที่ต้องการ')
    required_qly = fields.Integer(string='จำนวนที่ต้องการซื้อ')
    required_reason = fields.Text(string='สาเหตุที่ต้องการขอซื้อ')

    employee_id = fields.Many2one('hr.employee', string='ผู้ขอซื้อ')

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

