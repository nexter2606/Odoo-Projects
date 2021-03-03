from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ProjectTask(models.Model):
    _inherit = 'project.task'


    def write(self, values):
        res = super().write(values)
        emails = []
        total_time = 0.0
        mail_template = self.env.ref(
            'clinic_management.follower_project_email_template')
        for item in self.message_follower_ids:
            emails.append(item.email)
        project = self.browse(self.id)
        hours = project.planned_hours
        perc = self.env['ir.config_parameter'].sudo(
        ).get_param('percentage', default=0)
        buffer = int(perc)/100
        extra = hours + buffer
        for i in reversed(project.timesheet_ids):
            total_time += i.unit_amount
        if total_time >= extra:
            mail_template.with_context({
                'email_to': emails[0],
                'email_cc': ", ".join(emails[1:]),
                'emp_name': item.partner_id.name,
            }).send_mail(self.id, force_send=True)
        return res

    def send_follower_email(self):
        emails = []
        mail_template = self.env.ref(
            'clinic_management.follower_project_email_template')
        for item in self.message_follower_ids:
            print("\n\n\n item email==========", item.email)
            emails.append(item.email)
        print("\n\n\n emails========", emails)
        mail_template.with_context({
            'email_to': emails[0],
            'email_cc': [mail for mail in emails[1:]],
            'emp_name': item.partner_id.name,
        }).send_mail(self.id, force_send=True)
        print("\n\n\n Success")


class ResConfigSetting(models.TransientModel):
    _inherit = 'res.config.settings'

    percentage = fields.Integer(string='Percentage:')
    @api.model
    def set_values(self):
        self.env['ir.config_parameter'].sudo().set_param(
            'percentage', self.percentage)
        super().set_values()

    @api.model
    def get_values(self):
        res = super().get_values()
        res['percentage'] = int(
            self.env['ir.config_parameter'].sudo().get_param('percentage', default=0))
        return res
