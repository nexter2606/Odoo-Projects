from odoo import models, fields,tools
from odoo.exceptions import ValidationError


class DemoSqlView(models.Model):
    _name = 'aspl.sql.view.demo'
    _description = 'Sql View Demo Class'
    _auto = False

    patient_id = fields.Many2one('aspl.patient',string='Patient')
    doctor_id = fields.Many2one('aspl.doctor',string='Doctor')
    visit_id = fields.Many2one('aspl.visit',string='Visit')
    visit_line_id = fields.Many2one('aspl.visit.line',string='Visit Line')
    appointment_id = fields.Many2one('aspl.appointment',string = 'Appointment')

    def init(self):
        # print("\n hello======================================")
        tools.drop_view_if_exists(self.env.cr, self._table)
        self._cr.execute(""" CREATE VIEW aspl_sql_view_demo AS (
            SELECT
                p.id as id,
                v.patient_id as patient_id,
                v.doctor_id as doctor_id,
                p.id as visit_patient,
                d.id as visit_doctor
            FROM
                aspl_visit as v,
                aspl_patient as p,
                aspl_doctor as d
            WHERE
                v.patient_id=p.id and
                v.doctor_id=d.id    
               
        )

    """)


    
# SELECT
# #                 SELECT
#                 v.id as id,
#                 v.patient_id as patient_id,
#                 v.doctor_id as doctor_id
#             FROM
#                 aspl_visit as v
               