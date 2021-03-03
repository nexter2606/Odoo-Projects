from odoo import models, fields,api
from datetime import datetime


class MassVisit(models.Model):
    _name = 'mass.visit'
    _description = 'Mass Visit Class'

    patient_ids = fields.Many2many('aspl.patient','patient_mass_visit','patient_col1','visit_col2',string = "Patient")
    doctor_id= fields.Many2one('doctor.team',string="Doctor")


    def create_mass_visit(self):
        visit = self.env['aspl.visit']
        vals={}
        for i in self.patient_ids:
            vals.update({
            'patient_id': i.id,  
            'doctor_team_id': self.doctor_id.id,
            })
            visit.create(vals)
            print("Successs")
            
        return True