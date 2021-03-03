from odoo import models, fields


class MyOrderLine(models.Model):
    _name = 'my.order.line'
    _description = 'My order Line'

    lead_id = fields.Many2one('crm.lead',string="Lead")
    product_id = fields.Many2one('product.product',string="Product")
    desc=fields.Char(string='Description')
    qty=fields.Integer(string='Quantity')
    price=fields.Float(string='Price')
    total=fields.Float(string='Total',default=0)
