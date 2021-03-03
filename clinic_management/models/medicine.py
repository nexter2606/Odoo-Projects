from odoo import models, fields


class Medicine(models.Model):
    _name = 'aspl.medicine'
    _description = 'Medicine Class'

    name = fields.Char(required = True) 
    code = fields.Char(string = "Code")
    description = fields.Char(string = "Description")
    price = fields.Float(string = "Price")

