from odoo import models, fields,api


class VisitLine(models.Model):
    _name = 'aspl.visit.line'
    _description = 'Visit Line Class'

    name = fields.Char() 
    medicine_id = fields.Many2one('aspl.medicine',string = "Medicine")
    qty = fields.Float(string = "Quantity")
    price = fields.Float(string = "Price")
    total_price = fields.Float(string = " Total Price",compute = '__calc_total_price__')
    final_price = fields.Float(string = " Final Price")
    description = fields.Char(string = "Description")

    visit_id = fields.Many2one('aspl.visit',string= "Visit")

    @api.onchange('medicine_id')
    def __change_qty__(self):
        self.qty = 1
        
        self.price= self.medicine_id.price
        self.description= self.medicine_id.description

    @api.depends('price','qty')  
    def __calc_total_price__(self):
        for data in self:
            data.total_price = data.price * data.qty      

