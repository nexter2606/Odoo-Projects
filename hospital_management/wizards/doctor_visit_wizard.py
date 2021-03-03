from odoo import  fields, models, _

class DoctorVisitWizard(models.TransientModel):
    _name = 'doctor.visit.wizard'
    _description = 'doctor visit wizard'


    patient_id = fields.Many2one('res.partner',string='Patient :')
    issue = fields.Text(string = 'Problems/Issues:')
    doctor_id = fields.Many2one('res.users',string = "Doctor :")


    def create_visit_doctor(self):
        print("\n\n\nself.patient id",self.patient_id)
        print("\n\n\nself.issue",self.issue)
        x = self.env['doctor.visit']
        print("\n\n\n x=========",x)
        vals = {
            'patient_id':self.patient_id.id,
            'issue':self.issue
        }
        print("\n\n\n before create",vals)
        x.create(vals)


        
        return True


  