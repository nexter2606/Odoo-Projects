from odoo import models, fields, api
from datetime import datetime
import base64


class Visit(models.Model):
    _name = 'aspl.visit'
    _inherit = 'mail.thread'
    _description = 'Visit Class'

    name = fields.Char()  # for sequence generation
    patient_id = fields.Many2one(
        'aspl.patient', string="Patient", required=True)
    doctor_id = fields.Many2one('aspl.doctor', string="Doctor")
    reason = fields.Char(string="Reason")
    diagnosis = fields.Char(string="Diagnosis")
    allergy = fields.Char(string="Allergy")
    state = fields.Selection([('waiting', 'Waiting'), ('being_seen', 'Being Seen'), (
        'left_without_seen', 'Left W/O Seen'), ('complete', 'Complete'), ('cancel', 'Cancel')], default='waiting')
    visit_line_ids = fields.One2many(
        'aspl.visit.line', 'visit_id', string="Visit Line")
    final_price = fields.Float(
        string=" Final Price", compute='change_final_price')
    doctor_team_id = fields.Many2one('doctor.team', string="Doctor Team")

    # create sequence
    @api.model
    def create(self, values):
        seq_id = self.env.ref('clinic_management.seq_visit')
        values['name'] = seq_id.next_by_id()
        record = super() . create(values)
        return record

    # state changes
    def to_being_seen(self):
        self.state = 'being_seen'

    def to_left_without_seen(self):
        self.state = 'left_without_seen'

    def to_complete(self):
        self.state = 'complete'

    def to_cancel(self):
        self.state = 'cancel'

    # change final price
    @api.depends('visit_line_ids')
    def change_final_price(self):
        final_price = 0
        visit_line = self.visit_line_ids
        for i in visit_line:
            final_price += i.total_price
        self.final_price = final_price

    # create a invoice in aspl.invoice model
    def create_customer_invoice(self):
        invoice = self.env['aspl.invoice']
        invoice_values = {}
        line_values = []
        for item in self.visit_line_ids:
            line_values.append(
                (0, 0, {
                    'medicine_id': item.medicine_id.id,
                    'qty': item.qty,
                    'price': item.price,
                    'description': item.description,
                })
            )
        invoice_values.update({
            'patient_id': self.patient_id.id,
            'invoice_line_ids': line_values
        })
        invoice_id = invoice.create(invoice_values)
        self.state = 'cancel'

    # create a invoice in account.move
    def save_invoice(self):
        partner = self.patient_id.partner_id
        invoice = self.env['account.move']
        now = datetime.now()

        journal = invoice._get_default_journal()
        invoice_values = {}
        inv_line_values = []

        for item in self.visit_line_ids:
            inv_line_values.append(
                (0, 0, {
                    'name': item.description,
                    'quantity': item.qty,
                    'price_unit': item.price,
                    # 'price_subtotal': 100,
                    # 'account_id':21
                })
            )
        invoice_values.update({
            'partner_id': partner.id,
            'invoice_date': now,
            'invoice_line_ids': inv_line_values,
            # 'currency_id':journal.company_id.currency_id.id,
            # 'journal_id':journal.id,
            # 'move_type':'entry',
            'move_type': 'out_invoice',
            'state': 'draft',
            'date': now
        })
        print("\n\n\n invoice vals==========", invoice_values)
        inv_id = invoice.create(invoice_values)
        print("\n\n\n inv id=====", inv_id)

        return inv_id.action_post()

    # for creating an attachment in ir.attachment model
    def get_attachment_pdf(self):
        pdf = self.env.ref('clinic_management.report_visit_card')._render_qweb_pdf(
            res_ids=self.ids)
        b64_pdf = base64.b64encode(pdf[0])
        name = "Visit Report"
        self.env['ir.attachment'].create({
            'name': name,
            'type': 'binary',
            'datas': b64_pdf,
            'res_model': self._name,
            'res_id': self.id,
            'mimetype': 'application/x-pdf'
        })
        print("\n\n\n SUCCESS")
        return True

    
