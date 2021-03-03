# -*- coding: utf-8 -*-
from odoo import http
from odoo import http, exceptions
from odoo.http import request
import json



class MetricsAPI(http.Controller):

    @http.route('/patient', type='json', auth='user')
    def metrics_patient(self, **kwargs):
        result=[]
        patient_obj=request.env['aspl.patient'].search([ ])
        for i in patient_obj:
                case = {'patient': i.name , 'email': i.email, 'mobile':i.mobile,'patient_id':i.id }
                result.append(case)

        return result


    