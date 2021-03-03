# -*- coding: utf-8 -*-
from odoo import http
from odoo import http, exceptions
from odoo.http import request
import json



class AppointmentController(http.Controller):

    @http.route('/appointment', type='json', auth='user')
    def appointment(self, **kwargs):
        result=[]
        appointment_obj=request.env['aspl.appointment'].search([ ])
        for i in appointment_obj:
                case = {'patient_name': i.patient_id.name , 'doctor_name': i.doctor_id.name, 'reason':i.reason,'arrival_time':i.arrival_time,'patient_id':i.id,'patient_record_id':i.patient_id.id }
                result.append(case)

        return result


    