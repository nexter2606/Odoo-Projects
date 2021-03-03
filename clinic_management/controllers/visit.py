import json
import logging

from odoo import http
from odoo.http import request



class Visit(http.Controller):

    @http.route(['/visit'], type='json', auth='user')
    def scheduling(self, pid=None, **kwargs):
        visit_list=[]
        visit_obj=request.env['aspl.visit'].search([ ])
        for i in visit_obj:
                case = {'patient': i.patient_id.name , 'doctor': i.doctor_id.name, 'reason':i.reason }
                visit_list.append(case)

        
        # for v in request.env['aspl.visit'].search_read([], ['patient_id', 'doctor_id', 'reason']):
        #     if v['doctor_id']!=False and v['reason']!=False:
        #         visit_list.append(v)
        # print("\n\n\n ccas",visit_list)
        

        # result['values'] = {
        #         'name': 'Jane',
        #         'doctor': 'Raj',
        #         'reason': 'Pain',
        #         } 

        return visit_list 
        







# visit_obj=request.env['aspl.visit'].search([ ])
#         for i in visit_obj:
#             name.append(i.patient_id.name)
#             doctor.append(i.doctor_id.name)
#             reason.append(i.reason)
        
        
#         print("\n result====",result)
#         print("\n name====",name)
#         print("\n doctor====",doctor)
#         print("\n reason====",reason)