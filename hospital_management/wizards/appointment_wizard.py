from odoo import  fields, models, _

class AppointmentWizard(models.TransientModel):
    _name = 'appointment.wizard'
    _description = 'appointment wizard'


    patient_id = fields.Many2one('res.partner',string='Patient ID:')
    issue = fields.Text(string = 'Problems/Issues:')
    date = fields.Date(string = 'Appointment Date:')
    age = fields.Integer(string = 'Age')
    

    def create_appointment(self):
        x = self.env['patient.appointment']
        values = {
            'patient_id':self.patient_id.id,
            'issue':self.issue,
            'date':self.date,
            'age':self.age,
        }
        appointment_id = x.create(values)
        return {
            'name':'Appointment',
            'type':'ir.actions.act_window',
            'res_model':'patient.appointment',
            'res_id':appointment_id.id,
            'view_mode':'form',
        }