from odoo import fields, models


class ActWindowView(models.Model):
    _inherit = 'ir.actions.act_window.view'

#     view_mode = fields.Selection(selection_add=[
#     ('hello_world', 'Hello World')
# ], ondelete={'hello_world': 'cascade'})
   
    view_mode = fields.Selection(selection_add=[('map', "Map")
], ondelete={'map': 'cascade'})