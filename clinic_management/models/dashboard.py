from odoo import models, fields,api


class Dashboard(models.AbstractModel):
    _inherit = 'board.board'


    state = fields.Selection([('waiting', 'Waiting'), ('being_seen', 'Being Seen'), (
        'left_without_seen', 'Left W/O Seen'), ('complete', 'Complete'), ('cancel', 'Cancel')], default='waiting')

    

    