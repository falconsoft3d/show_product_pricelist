# -*- coding: utf-8 -*-
from odoo import api, models, fields

class SppResCompany(models.Model):
    _inherit = "res.company"

    pricelist_id = fields.Many2one('product.pricelist', 'Lista de Precios')
