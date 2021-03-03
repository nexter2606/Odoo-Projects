# -*- coding: utf-8 -*-

from odoo import models, fields,api
from datetime import datetime


class Appointment(models.Model):
    _name = 'aspl.appointment'
    _description = 'Appointment Class'

    name = fields.Char() #for sequence generation
    patient_id = fields.Many2one('aspl.patient',string = "Patient",required = True)
    doctor_id = fields.Many2one('aspl.doctor',string = "Doctor")
    reason = fields.Char(string = "Reason")
    arrival_time = fields.Datetime(string = "Arrived Time")
    leaving_time = fields.Datetime(string = "Leaving Time")
    state = fields.Selection([('booked', 'Booked'), ('arrived', 'Arrived'),('cancel', 'Cancel'), ], default='booked')
    progress_rate = fields.Integer()
    maximum_rate = fields.Integer()

    # generate Appointment Sequence
    @api.model
    def create(self,values):
        seq_id = self.env.ref('clinic_management.seq_appointment')  
        values['name'] = seq_id.next_by_id() 
        record = super () . create(values)
        return record

    # Fill arrived time field at button click
    def to_arrived(self):
        self.state = 'arrived'
        now = datetime.now()
        self.arrival_time = now

    # change state cancel
    def to_cancel(self):
        self.state = 'cancel'

    # create patient visit if doctor is selected create a visit or take doc input and then create 
    def create_visit(self):
        visit = self.env['aspl.visit']
        values = {
            'patient_id':self.patient_id.id,
            'doctor_id':self.doctor_id.id,
            'reason': self.reason
        }
                
        action = {
            'name': " Create Appointment Wizard",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'create.appointment.wizard',
            'view_id': self.env.ref('clinic_management.appointment_wizard_form').id,
            'target': 'new',
            'context':{'default_patient_id':self.patient_id.id,'default_reason':self.reason}
        }
        if self.doctor_id:
            visit.create(values)
        else:
            return action

    


    



