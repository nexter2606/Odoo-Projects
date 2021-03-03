from odoo import fields, models


class ProjectPdfReport(models.AbstractModel):

    _name = 'report.aspl_product_commision.report_project'
    _description = ' project pdf report generation class'

    user_ids = fields.Many2many(
        'res.users', 'user_prj', 'user_1', 'prj22', string="Users")
    start_date = fields.Datetime(string="Start Date")
    end_date = fields.Datetime(string="End Date")
    project_ids = fields.Many2many(
        'project.project', 'proj', 'proj1', 'proj2', string="Project")

    def _get_report_values(self, docids, data=None):
        wizard_obj = self.env['project.wizard'].browse(docids[0])
        dict1={}
        list1 = []
        for user in wizard_obj.user_ids:
            print("\n\n\n user==========",user)
            task = self.env['project.task'].search([('create_date', '>', wizard_obj.start_date),
                                                              ('create_date', '<',
                                                               wizard_obj.end_date),
                                                              ('user_id', '=', user.id),('project_id', 'in', wizard_obj.project_ids.ids)])
        
        
            for data in task.timesheet_ids:
                if data.user_id.id == user.id:
                    list1.append([data.date, data.employee_id.name, data.name, data.unit_amount])
                    dict1.update({
                        user.name:list1
                    })
            list1=[]      
        print("\n\n\n dict1=======",dict1)                                                        

        return{
            'dict1':dict1

        }    
