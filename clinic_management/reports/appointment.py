from odoo import fields, models,api


class AppointmentPdfReport(models.AbstractModel):

    _name = 'report.clinic_management.report_appointment'
    _description = ' patient appointment pdf report generation class'

    patient_id = fields.Many2one('aspl.patient',string = "Patient",required = True)
    doctor_id = fields.Many2one('aspl.doctor',string = "Doctor")
    reason = fields.Char(string = "Reason")
    arrival_time = fields.Datetime(string = "Arrived Time")
    state = fields.Selection([('booked', 'Booked'), ('arrived', 'Arrived'),('cancel', 'Cancel'), ], default='booked')

    

    def _get_report_values(self, docids, data=None):
        
        wizard = self.env['appointment.report.wizard'].browse(docids[0])
        # print("\n\n\n wizard===",wizard)
        # print("\n\n\ docids",docids)

        for i in wizard.patient_ids:
            print("\n\n\n pat name==",i.name)
        
        appointment = self.env['aspl.appointment'].search([('state','=',wizard.state),
            ('patient_id','in',wizard.patient_ids.ids),
            ('doctor_id','in',wizard.doctor_ids.ids),
            ('create_date','>',wizard.start_date),
            ('create_date','<',wizard.end_date),
            
            ])
        
        return{
            'patient_id':self.patient_id,
            'doctor_id':self.doctor_id,
            'appointment':appointment
        }



