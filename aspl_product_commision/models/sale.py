# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrderLIne(models.Model):
    _inherit = 'sale.order.line'

    lead_id = fields.Many2one('crm.lead', string='Lead')


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    commision_ids = fields.One2many(
        'commision.details', 'sale_id', string="Commision Details")

    def testing_commision(self):
        line_values = []
        for i in self.order_line:
            for item in i.product_id.commision_ids:
                if self.user_id.id == item.user_id.id:
                    line_values.append(
                        (0, 0, {
                            'user_id': item.user_id.id,
                            'amount': item.amount,
                        })
                    )
        self.write({
            'id': self.id,
            'commision_ids': line_values})
        print("\n\n\n\n success")
        return True
    

    # commented so it cant interfere
    # def _action_confirm(self):
    #     res = super()._action_confirm()
    #     line_values = []
    #     for i in self.order_line:
    #         for item in i.product_id.commision_ids:
    #             if self.user_id.id == item.user_id.id:
    #                 line_values.append(
    #                     (0, 0, {
    #                         'user_id': item.user_id.id,
    #                         'amount': item.amount,
    #                     })
    #                 )
    #     self.write({
    #         'id': self.id,
    #         'commision_ids': line_values})

    #     return res

    def get_quotations(self):
        action = {
            'name': 'Quotation Details',
            'domain': [ ('partner_id','=',self.partner_id.id)  ],
            'view_type': 'form',
            'res_model': 'crm.lead',
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }
        return action
