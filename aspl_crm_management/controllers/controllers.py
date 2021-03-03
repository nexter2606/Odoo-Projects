# -*- coding: utf-8 -*-
# from odoo import http


# class AsplCrmManagement(http.Controller):
#     @http.route('/aspl_crm_management/aspl_crm_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aspl_crm_management/aspl_crm_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aspl_crm_management.listing', {
#             'root': '/aspl_crm_management/aspl_crm_management',
#             'objects': http.request.env['aspl_crm_management.aspl_crm_management'].search([]),
#         })

#     @http.route('/aspl_crm_management/aspl_crm_management/objects/<model("aspl_crm_management.aspl_crm_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aspl_crm_management.object', {
#             'object': obj
#         })
