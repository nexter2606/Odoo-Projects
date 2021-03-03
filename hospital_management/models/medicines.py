from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    
    is_medicine = fields.Boolean(string='Is Medicine' )
    doctor_id = fields.Many2one('doctor.visit',string = "Doctor :")
    # doctor_visit_line_ids = fields.One2many('doctor.visit.line','medicine_id',string = "Doctor Visit Line :")
    
    quantity = fields.Integer(string = "Quantity:" , default = "1")
    total_cost = fields.Float(string = "Total Cost:" , compute = "get_total_cost" )


    # @api.model
    # def name_search(self, name='', args=None, operator='ilike', limit=100):
        
    #     args=[('is_medicine','=',True)]       
    #     rec = super (ProductTemplate , self). name_search(name,args,operator,limit)
    #     return rec

    @api.depends('quantity','standard_price')
    def get_total_cost(self):
        self.total_cost = 0
        if self.quantity and self.standard_price:
            self.total_cost = self.quantity * self.standard_price
