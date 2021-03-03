# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    user_ids = fields.Many2many('res.users','user_emp_data','user_data','emp_data')

    def show_records(self):
       
        employee_id = self.env['hr.employee'].search([('user_id','=',self.id)])
        print ("\n employee_id >>>>>>>>>>>>>. ",employee_id.name,employee_id)
            
        employee_ids = self.env['hr.employee'].search([('parent_id','=',employee_id.id)])
        user_ids = [employee_id.user_id.id for employee_id in employee_ids if employee_id.user_id]

        self.user_ids = user_ids
                
        return True
