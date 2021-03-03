from odoo import models, fields


class Doctor(models.Model):
    _name = 'aspl.doctor'
    _description = 'Doctor Class'

    partner_id = fields.Many2one('res.partner', delegate=True, required=True, ondelete='cascade')

    # show patients having appointment for specific doctor
    def get_patient_appointment(self):
        return {
            'name': 'Patient Appointments',
            'domain': [('doctor_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'aspl.appointment',
            'view_mode': 'tree,form,calendar',
            'type': 'ir.actions.act_window',
        }
    