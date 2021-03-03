# -*- coding: utf-8 -*-

from odoo import models, fields,api
from odoo.exceptions import ValidationError


class Patient(models.Model):
    _name = 'aspl.patient'
    _description = 'Patient Class'

    partner_id = fields.Many2one('res.partner', delegate=True, required=True, ondelete='cascade')
    appointment_id = fields.Many2one('aspl.appointment',string = 'Appointment')

    def get_appointment(self):
        return {
            'name': 'Patient Appointment',
            'domain': [('patient_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'aspl.appointment',
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }
    
    def send_email(self):
        mail_template = self.env.ref('clinic_management.patient_email_template')
        mail_template.send_mail(self.id, force_send=True)
        print("\n\n\n Success")    

# send mail with context and use them in the template
# def project_send_email(self):
#         mail_template = self.env.ref('clinic_management.project_email_template')
#         project=self.env['project.task'].browse(12)
#         hours=project.planned_hours
#         total_time=0
#         for i in reversed(project.timesheet_ids):
#             total_time+=i.unit_amount
#             if total_time>hours:
#                 mail_template.with_context({
#                 'email_to':i.employee_id.work_email ,
#                 'emp_name':i.employee_id.name,
#                 'extra_working_time':i.unit_amount 
#                 }).send_mail(self.id,force_send=True)
#                 print("\n\n\n Success")  