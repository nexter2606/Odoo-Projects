from odoo import models, fields


class Demo(models.Model):
    _name = 'aspl.demo'
    _description = 'Demo Testing Class'

    name=fields.Char(string='Name')