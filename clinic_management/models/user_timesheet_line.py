from odoo import models, fields, api


class UserTimesheetLine(models.Model):
    _name = 'user.timesheet.line'
    _description = 'User Timesheet Line'

    date = fields.Date(string='Date')
    duration = fields.Float(string='Total Hours')
    description = fields.Char(string='Description')
    timesheets_id = fields.Many2one('user.timesheet',string='Timesheet')