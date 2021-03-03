from odoo import models, fields
import tempfile
import base64
import binascii
import xlsxwriter


class SaveData(models.Model):

    _name = 'save.report.wizard'
    _description = 'save report wizard class'

    name = fields.Char(string='Name')
    file = fields.Binary(string='File')


class ProjectTaskWizard(models.TransientModel):
    _name = 'project.wizard'
    _description = 'Project Wizard'

    user_ids = fields.Many2many(
        'res.users', 'user_prj', 'user_1', 'prj22', string="Users")
    start_date = fields.Datetime(string="Start Date")
    end_date = fields.Datetime(string="End Date")
    project_ids = fields.Many2many(
        'project.project', 'proj', 'proj1', 'proj2', string="Project")

    def get_pdf_report(self):
        return self.env.ref('aspl_product_commision.report_project_card').report_action(self)

    def get_excel_report(self):
        file_path = tempfile.NamedTemporaryFile(suffix=".xls").name
        task = self.env['project.task']

        workbook = xlsxwriter.Workbook(file_path)
        worksheet = workbook.add_worksheet()
        cell_format = workbook.add_format(
            {'bold': True, 'font_color': 'blue', 'bg_color': 'yellow', 'align': 'center'})
        merge_format = workbook.add_format(
            {'align': 'center', 'bg_color': 'red'})
        cell_format2 = workbook.add_format(
            {'font_color': 'blue', 'align': 'center'})

        row = 1
        col = 0
        

        worksheet.set_column(4, 4, 25)
        worksheet.set_column(2, 2, 25)
        worksheet.set_column(1, 1, 25)
        worksheet.set_column(3, 3, 25)

        dict1 = {}
        list1 = []
        for user in self.user_ids:
            task = self.env['project.task'].search([('create_date', '>', self.start_date),
                                                    ('create_date', '<',
                                                     self.end_date),
                                                    ('user_id', '=', user.id), ('project_id', 'in', self.project_ids.ids)])

            for data in task.timesheet_ids:
                if data.user_id.id == user.id:
                    list1.append([data.date, data.employee_id.name,
                                  data.name, data.unit_amount])
                    dict1.update({
                        user.name: list1
                    })
            list1 = []

        for k, v in dict1.items():
            worksheet.merge_range('A1:D1', 'Project Data', merge_format)
            worksheet.write(row, col, 'Date', cell_format)
            worksheet.write(row, col+1, 'Employee', cell_format)
            worksheet.write(row, col+2, 'Description', cell_format)
            worksheet.write(row, col+3, 'Hours', cell_format)
            row += 1
            for j in v:
                if k == j[1]:
                    worksheet.write(row, col, str(j[0]), cell_format2)
                    worksheet.write(row, col+1, j[1], cell_format2)
                    worksheet.write(row, col+2, j[2], cell_format2)
                    worksheet.write(row, col+3, j[3], cell_format2)
                    row += 1



        workbook.close()
        buf = base64.encodebytes(open(file_path, 'rb').read())
        report_rec = self.env['save.report.wizard'].create(
            {'file': buf, 'name': 'Project Report.xls'})
        action = {
            'name': " Project Wizard",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'save.report.wizard',
            'res_id': report_rec.id,
            'target': 'new'
        }
        return action
