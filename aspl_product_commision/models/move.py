from odoo import models, fields, api

class AccountPaymentRegister(models.TransientModel):
    _inherit = 'account.payment.register'

    def action_create_payments(self):
        res = super().action_create_payments()
        invoice = self.env['account.move'].browse(self._context.get('active_ids'))
        user=invoice.partner_id
        user_search = self.env['res.users'].search([ ('partner_id','=',user.id)])
        commision=self.env['commision.details'].search([ ('user_id','=',user_search.id) ])
        for i in commision:
            i.status='register'
        return res





