# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)


class BagType(models.Model):
    _name = 'si.sag.type'
    _description = 'FMD Sag Type'

    name = fields.Char(string='ประเภทกระสอบ', required=True)
    weight = fields.Float(string='นํ้าหนักกระสอบ (kg)', required=True)
    description = fields.Text(string='คำอธิบาย')
    update_date = fields.Datetime(string='วันที่ปรับปรุง', default=fields.Datetime.now, readonly=True)
