from odoo import fields, models, _
import xlsxwriter, tempfile, base64,xlrd,openpyxl


class SaveData(models.Model):

    _name = 'save.report.wizard'
    _description = 'save report wizard class'

    name = fields.Char(string='Name')
    file = fields.Binary(string='File')


class AppointmentReportWizard(models.TransientModel):

    _name = 'appointment.report.wizard'
    _description = ' Create Appointment Report XLX Wizard'

    patient_ids = fields.Many2many('aspl.patient','patient_appointment','patient_col1','patient_col2',string = "Patient")
    doctor_ids = fields.Many2many('aspl.doctor','doctor_appointment','doctor_col1','doctor_col2',string = "Doctor")
    start_date = fields.Datetime(string = "Start Date",required=True)
    end_date = fields.Datetime(string = "End Date" ,required=True)
    state = fields.Selection([('booked', 'Booked'), ('arrived', 'Arrived'),('cancel', 'Cancel'), ], default='booked')

    # xls report
    def get_report(self):
        file_path = tempfile.NamedTemporaryFile(suffix=".xls").name

        workbook = xlsxwriter.Workbook(file_path)
        worksheet = workbook.add_worksheet()
        cell_format = workbook.add_format({ 'bold': True,'font_color': 'blue','bg_color':'yellow','align':'center'})
        merge_format = workbook.add_format({'align': 'center','bg_color':'red'})
        cell_format2 = workbook.add_format({ 'font_color': 'blue','align':'center'})

        row = 1
        col = 0
        worksheet.merge_range('A1:D1', 'Appointment Data', merge_format)
        worksheet.write(row,col, 'Patient Name',cell_format) 
        worksheet.write(row,col+1, 'Doctor Name',cell_format) 
        worksheet.write(row,col+2, 'State',cell_format) 
        worksheet.write(row,col+3, 'Arrival Time',cell_format) 
        row+=1

        worksheet.set_column(4, 4, 25)
        worksheet.set_column(2, 2, 25)
        worksheet.set_column(1, 1, 25)
        worksheet.set_column(3, 3, 25)

        #search in appointment and get records
        appointment = self.env['aspl.appointment'].search([('state','=',self.state),
            ('patient_id','in',self.patient_ids.ids),
            ('doctor_id','in',self.doctor_ids.ids),
            ('create_date','>',self.start_date),
            ('create_date','<',self.end_date),
            ])

        for i in appointment:
            worksheet.write(row, col, i.patient_id.name,cell_format2)
            worksheet.write(row, col+1, i.doctor_id.name,cell_format2)
            worksheet.write(row, col+2, i.state,cell_format2)
            worksheet.write(row, col+3, i.arrival_time,cell_format2)
            row +=1
        
        workbook.close()
        buf=base64.encodebytes(open(file_path ,'rb').read())

        report_rec=self.env['save.report.wizard'].create({'file':buf,'name':'Patient Appointment Report.xls'})
        action = {
            'name': " Save Patient Appointment Wizard",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'save.report.wizard',
            'res_id': report_rec.id,
            'target': 'new'
        }
        return action
    
    def get_pdf_report(self):
        return self.env.ref('clinic_management.report_appointment_card').report_action(self)
    
    
    




       

   
   
   



   