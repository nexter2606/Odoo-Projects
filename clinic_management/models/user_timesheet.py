from odoo import models, fields, api


class UserTimesheet(models.Model):
    _name = 'user.timesheet'
    _description = 'User Timesheet'

    timesheet_line_ids = fields.One2many(
        'user.timesheet.line', 'timesheets_id', string='Timesheet Line')
    user_id = fields.Many2one('res.users', string='Assigned To', required=True)
    project_id = fields.Many2one('project.project', string='Project')
    task_id = fields.Many2one('project.task', string='Task')
    total_time = fields.Float(string='Total Hours')

    @api.onchange('user_id', 'project_id', 'task_id')
    def change_data(self):
        if self.user_id:
            lines = [(5,)]
            vals = {}
            my_time = 0
            task = self.env['project.task'].search(
                ['|', '|', ('user_id', '=', self.user_id.id), ('project_id', '=', self.project_id.id), ('name', '=', self.task_id.name)])
            for record in task:
                for item in record.timesheet_ids:
                    my_time += item.unit_amount
                    lines.append(
                        (0, 0, {
                            'date': item.date,
                            'duration': item.unit_amount,
                            'description': item.name,
                        })
                    )
            vals.update({
                'timesheet_line_ids': lines,
                'total_time': my_time
            })
            self.write(vals)
