from odoo import fields, models
import html,inspect
from bs4 import BeautifulSoup


class ChatterVisitPdfReport(models.AbstractModel):

    _name = 'report.clinic_management.report_chatter'
    _description = ' chatter visit pdf report generation class'

    name = fields.Char(string='Name:')
    patient_id = fields.Many2one('aspl.patient',string = "Patient")

    def _get_report_values(self, docids, data=None):
        messege = self.env['aspl.visit'].browse(docids[0])
        chatters = []
        for i in messege:
            for item in i.message_ids:
                soup = BeautifulSoup(item.body,features="lxml")
                chatters.append(soup.get_text())
        return{
            'chatter':chatters,
            'user':self.env.user,
            'display':messege.name
        }



