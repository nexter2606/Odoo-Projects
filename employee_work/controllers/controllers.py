# -*- coding: utf-8 -*-
# from odoo import http


# class EmployeeWork(http.Controller):
#     @http.route('/employee_work/employee_work/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employee_work/employee_work/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('employee_work.listing', {
#             'root': '/employee_work/employee_work',
#             'objects': http.request.env['employee_work.employee_work'].search([]),
#         })

#     @http.route('/employee_work/employee_work/objects/<model("employee_work.employee_work"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employee_work.object', {
#             'object': obj
#         })
