# -*- coding: utf-8 -*-

from odoo import models, fields,api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    verified = fields.Boolean(string='Verified')
    approved = fields.Boolean(string='Approved')

    @api.onchange('approved')
    def change_approved(self):
        if self.approved:
            self.verified=True
        else:
            self.verified=False    


    