from odoo import fields, models, _
import tempfile, base64,xlrd,binascii
import csv
import struct
import numpy as np


class CreateCsvData(models.TransientModel):

    _name = 'create.csv.records.wizard'
    _description = 'create csv records wizard class'

    name = fields.Char(string='Name')
    file = fields.Binary(string='File')

    def get_data(self):
        patient = self.env['aspl.patient']
        vals={}
        with open('/home/nisarg/Nisarg/address.csv', 'r') as file1:
            reader = csv.reader(file1)
            
            patient_email=[]
            for i in patient.search([('email','!=',False)]):
                patient_email.append(i.email)
            
            for row in reader:
                if row[4] not in patient_email:
                    vals.update({
                        'name':row[0],
                        'mobile':row[1],
                        'street':row[2],
                        'city':row[3],
                        'email':row[4],
                    })
                    patient.create(vals)
                    print("\n Success")

             


        return True
    
