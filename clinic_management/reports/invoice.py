from odoo import fields, models,api


class InvoicePdfReport(models.AbstractModel):

    _name = 'report.clinic_management.report_invoice'
    _description = ' patient invoice pdf report generation class'

    name = fields.Char(string='Name:')
    patient_id = fields.Many2one('aspl.patient',string = "Patient")

    

    def _get_report_values(self, docids, data=None):
        docs = self.env['aspl.invoice'].browse(docids[0])



        
        return{
            'docs':docs,
            'patient_id':self.patient_id,
            'invoice_line_ids': docs.invoice_line_ids
            
        }



