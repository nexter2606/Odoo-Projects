from odoo import models, fields,api


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    order_line_ids = fields.One2many(
        'my.order.line', 'lead_id', string="Commision")


    def action_new_quotation(self):
        action = super().action_new_quotation() 
        data1 = []
        for item in self.order_line_ids:
            data1.append(
                (0, 0, {
                    'name': item.desc,
                    'product_id': item.product_id.id,
                    'product_uom_qty': item.qty,
                    'price_unit': item.price,
                    'customer_lead':100,
                    'order_id':1,
                    'price_subtotal':item.price*item.qty,
                    'lead_id':item.lead_id.id,
                    'product_uom':1
                })
            )
        print("\n\n\n data======",data1)    
        action['context'].update({
            'default_order_line': data1
        })
        return action
