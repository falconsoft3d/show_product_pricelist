# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class SppProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.multi
    @api.depends('item_ids')
    def _get_pricelist_price(self):
        default_pricelist = self.env.user.company_id.pricelist_id
        for template in self:
            if default_pricelist:
                pricelist_item = template.item_ids.filtered(lambda r: r.pricelist_id == default_pricelist)
                for item in pricelist_item:
                    template.pricelist_price = item.pricelist_id.get_product_price(template, 1.0, None)

    def _set_pricelist_price(self):
        default_pricelist = self.env.user.company_id.pricelist_id
        for template in self:
            if template.pricelist_price > 0.0:
                if template.item_ids:
                    for item in template.item_ids:
                        if item.product_tmpl_id == template:
                            item.write({
                                'compute_price': 'fixed',
                                'fixed_price': template.pricelist_price,
                                'price_surcharge': 0.0
                            })
                        else:
                            self.env['product.pricelist.item'].create({
                                'applied_on': '1_product',
                                'product_tmpl_id': template.id,
                                'compute_price': 'fixed',
                                'fixed_price': template.pricelist_price,
                                'pricelist_id': default_pricelist.id
                            })
                else:
                    self.env['product.pricelist.item'].create({
                            'applied_on': '1_product',
                            'product_tmpl_id': template.id,
                            'compute_price': 'fixed',
                            'fixed_price': template.pricelist_price,
                            'pricelist_id': default_pricelist.id
                    })

    pricelist_price = fields.Monetary("Price List", compute="_get_pricelist_price", inverse="_set_pricelist_price")

class SppProductProduct(models.Model):
    _inherit = 'product.product'

    @api.multi
    @api.depends('pricelist_item_ids')
    def _get_pricelist_price(self):
        default_pricelist = self.env.user.company_id.pricelist_id
        for product in self:
            if default_pricelist:
                pricelist_item = product.pricelist_item_ids.filtered(lambda r: r.pricelist_id == default_pricelist)
                for item in pricelist_item:
                    product.pricelist_price = item.pricelist_id.get_product_price(product, 1.0, None)

    def _set_pricelist_price(self):
        default_pricelist = self.env.user.company_id.pricelist_id
        for product in self:
            if product.pricelist_price > 0.0:
                if product.pricelist_item_ids:
                    for item in product.pricelist_item_ids:
                        if item.product_id == product:
                            item.write({
                                'compute_price': 'fixed',
                                'fixed_price': product.pricelist_price,
                                'price_surcharge': 0.0
                            })
                        else:
                            self.env['product.pricelist.item'].create({
                                'applied_on': '0_product_variant',
                                'product_id': product.id,
                                'compute_price': 'fixed',
                                'fixed_price': product.pricelist_price,
                                'pricelist_id': default_pricelist.id
                            })
                else:
                    self.env['product.pricelist.item'].create({
                            'applied_on': '0_product_variant',
                            'product_id': product.id,
                            'compute_price': 'fixed',
                            'fixed_price': product.pricelist_price,
                            'pricelist_id': default_pricelist.id
                    })
    
    pricelist_price = fields.Float("Price List", compute="_get_pricelist_price", inverse="_set_pricelist_price")
