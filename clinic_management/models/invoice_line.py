# -*- coding: utf-8 -*-

from odoo import models, fields,api


class InvoiceLine(models.Model):
    _name = 'aspl.invoice.line'
    _description = 'Invoice Line Class'


    invoice_id = fields.Many2one('aspl.invoice',string="Invoice")
    medicine_id = fields.Many2one('aspl.medicine',string="Medicine")
    qty = fields.Float(string = "Quantity")
    price = fields.Float(string = "Price")
    total_price = fields.Float(string = " Total Price",compute='change_total_price')
    final_price = fields.Float(string = " Final Price")
    description = fields.Char(string = "Description")

    @api.depends('qty','price')
    def change_total_price(self):
        for value in self:
            value.total_price = value.price * value.qty    

    





