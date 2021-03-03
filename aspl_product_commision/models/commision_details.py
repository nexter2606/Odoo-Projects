from odoo import models, fields


class CommisionDetails(models.Model):
    _name = 'commision.details'
    _description = 'commision details'

    user_id = fields.Many2one('res.users',string="User")
    comp_price = fields.Selection([('fix', 'Fix'), ('perc', 'Percentage'), ], default='fix')
    amount = fields.Float(string="Commision Amount")
    status = fields.Selection([('draft', 'Draft'), ('billed', 'Billed'), ('register', 'Register'),], default='draft')

    product_id = fields.Many2one('product.product',string="Product")
    sale_id = fields.Many2one('sale.order',string="Sale")
    invoice_id = fields.Many2one('account.move',string="Invoice")


    