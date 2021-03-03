from odoo import api, fields, models, _
import json
from lxml import etree



class ResPartner(models.Model):
    _inherit = 'res.partner'

    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female'), ('others', 'Others'), ])
    
    is_patient = fields.Boolean(string='Is Patient')
    is_nurse = fields.Boolean(string='Is Nurse')
    salary = fields.Float(string = "Salary:")
    
    appointment_ids = fields.One2many('patient.appointment','patient_id', string = 'Appointments :')

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        
        args=[('is_patient','=',True)]       
        rec = super (ResPartner , self). name_search(name,args,operator,limit)
        return rec

    # def open_appointment_wizard(self):
    #     action = {
    #             'name': _('Wizard Appointment View'),
    #             'view_mode': 'tree,form',
    #             'res_model': 'res.partner',
    #             'res_id': self.env.ref('hospital_management.appointment_wizard_custom_tree_view').id,
    #             'type': 'ir.actions.act_window',
    #             'target': 'current',
                
    #         }
    #     return action

    @api.onchange('function')
    def change_salary(self):
        if self.function == 'CEO':
            self.salary = 54000
        elif self.function == 'CTO':
            self.salary = 50000
        elif self.function == 'Director':
            self.salary = 100000        
    
    


    def create_appointment(self):
        view_id = self.env.ref('hospital_management.appointment_wizard_form')
        return {
            'name':'Register an Appointment',
            'type':'ir.actions.act_window',
            'res_model':'appointment.wizard',
            'view_mode':'form',
            'target':'new',
            'view_id':view_id.id,
            'context':{'default_patient_id':self.id  }
        }

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super().fields_view_get(view_id, view_type, toolbar, submenu)
        if view_type=='form' and self._context.get('default_is_patient'):
            doc = etree.XML(res['arch'])
            for node in doc.xpath("//field[@name='mobile']"):
                node.set("required", "1")
                modifiers = json.loads(node.get("modifiers"))
                modifiers['required'] = True
                node.set("modifiers", json.dumps(modifiers))
            for node in doc.xpath("//field[@name='company_type']"):
                node.set("invisible", "1")
                modifiers = json.loads(node.get("modifiers"))
                modifiers['invisible'] = True
                node.set("modifiers", json.dumps(modifiers))
            res['arch'] = etree.tostring(doc)
        return res    