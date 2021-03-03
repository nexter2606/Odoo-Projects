# -*- coding: utf-8 -*-

from odoo import models, fields,api
import base64


class Invoice(models.Model):
    _name = 'aspl.invoice'
    _description = 'Invoice Class'

    name = fields.Char() #for seq!

    invoice_line_ids = fields.One2many('aspl.invoice.line','invoice_id',string = "Invoice Line")
    patient_id = fields.Many2one('aspl.patient',string = "Patient",required = True)
    total_amount = fields.Float(string = " Total Amount ",compute = '__change_total_amount__')
    invoice_date = fields.Datetime(string = "Invoice Date")
    payment_date = fields.Datetime(string = "Payment Date")
    status = fields.Selection([('draft', 'Draft'), ('validated', 'Validated'),('paid', 'Paid'),('cancel', 'Cancel'), ], default='draft')

    def to_validate(self):
        self.status = 'validated'
    
    def to_paid(self):
        self.status = 'paid'
    
    def to_cancel(self):
        self.status = 'cancel'

    @api.model
    def create(self,values):
        seq_id = self.env.ref('clinic_management.seq_invoice')  
        values['name'] = seq_id.next_by_id() 
        record = super () . create(values)
        return record

    @api.depends('invoice_line_ids') 
    def __change_total_amount__(self):
        total = 0
        for i in self.invoice_line_ids:
            total += i.total_price
        self.total_amount = total   

    def print_report(self):
        return self.env.ref('clinic_management.report_invoice_card').report_action(self)
        



