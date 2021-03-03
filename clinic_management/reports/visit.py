from odoo import fields, models,api


class VisitPdfReport(models.AbstractModel):

    _name = 'report.clinic_management.report_visit'
    _description = ' patient visit pdf report generation class'

    name = fields.Char(string='Name:')
    patient_id = fields.Many2one('aspl.patient',string = "Patient")

    

    def _get_report_values(self, docids, data=None):
        docs = self.env['aspl.visit'].browse(docids[0])
        print("\n\n\n docs=====",docs)
        return{
            'name':self.name,
            'patient_id':self.patient_id,
            'docs':docs,
            'visit_line_ids':docs.visit_line_ids
            
        }



