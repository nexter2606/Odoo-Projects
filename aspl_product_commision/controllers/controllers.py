# -*- coding: utf-8 -*-
# from odoo import http


# class AsplProductCommision(http.Controller):
#     @http.route('/aspl_product_commision/aspl_product_commision/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aspl_product_commision/aspl_product_commision/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aspl_product_commision.listing', {
#             'root': '/aspl_product_commision/aspl_product_commision',
#             'objects': http.request.env['aspl_product_commision.aspl_product_commision'].search([]),
#         })

#     @http.route('/aspl_product_commision/aspl_product_commision/objects/<model("aspl_product_commision.aspl_product_commision"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aspl_product_commision.object', {
#             'object': obj
#         })
