from odoo import models, fields
from datetime import datetime


class RegisterPayment(models.TransientModel):
    _name = 'register.payment'
    _description = 'register payment wizard for use in sale bill generation'

    user_ids = fields.Many2many(
        'res.users', 'user_reg_pay', 'user1', 'reg_pay2', string="Users")
    start_date = fields.Datetime(string="Start Date")
    end_date = fields.Datetime(string="End Date")

    def get_common_records(self):
        vals = {}
        list1 = []
        invoice = self.env['account.move']
        journal = invoice._get_default_journal().id

        for user in self.user_ids:
            commision = self.env['commision.details'].search([('create_date', '>', self.start_date),
                                                              ('create_date', '<',
                                                               self.end_date),
                                                              ('user_id', '=', user.id)])
            for value in commision:
                value.status='billed'
                list1.append(value.amount)
            vals.update({
                'partner_id': user.partner_id.id,
                'invoice_line_ids': [(
                    0, 0, {
                        'name': 'Commision',
                        'price_unit': sum(list1),
                        'quantity': 1,
                        'account_id': journal
                    }
                )],
                'move_type': 'in_invoice',
                'state': 'draft',
            })
            record = invoice.create(vals)
            print("\n\n\n record======", record)
            vals = {}

            
            
