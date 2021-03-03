from odoo import models, fields,api
from datetime import datetime


class DoctorTeam(models.Model):
    _name = 'doctor.team'
    _description = 'Doctor Team Class'

    name = fields.Char(string="Name") 
    doctor_ids = fields.Many2many('aspl.doctor','patient_doctor','patient_col','doctor_col',string = "Doctor")
    