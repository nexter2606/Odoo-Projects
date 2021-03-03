from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    commision_ids = fields.One2many('commision.details','product_id',string="Commision Details")