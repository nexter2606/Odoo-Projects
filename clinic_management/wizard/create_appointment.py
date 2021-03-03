from odoo import fields, models, _


class CreateAppointmentWizard(models.TransientModel):

    _name = 'create.appointment.wizard'
    _description = ' Create Appointment Wizard'

    patient_id = fields.Many2one('aspl.patient',string = "Patient")
    doctor_id = fields.Many2one('aspl.doctor',string = "Doctor")
    reason = fields.Char(string = "Reason")

    def get_records(self):
        visit = self.env['aspl.visit']
        appointment = self.env['aspl.appointment'].browse(self._context.get('active_ids', []))
        values = {
            'doctor_id':self.doctor_id.id,
        }
        create_id = visit.create(values)
        
        return {
            'name':'Visit',
            'type':'ir.actions.act_window',
            'res_model':'aspl.visit',
            'res_id':create_id.id,
            'view_mode':'form',
        }
        
        


    
    
    
    
    
   




       

   
   
   



   