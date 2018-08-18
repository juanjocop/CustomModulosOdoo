# -*- coding: utf-8 -*-
from odoo import http

# class Ecoworldpaginas(http.Controller):
#     @http.route('/ecoworldpaginas/ecoworldpaginas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ecoworldpaginas/ecoworldpaginas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ecoworldpaginas.listing', {
#             'root': '/ecoworldpaginas/ecoworldpaginas',
#             'objects': http.request.env['ecoworldpaginas.ecoworldpaginas'].search([]),
#         })

#     @http.route('/ecoworldpaginas/ecoworldpaginas/objects/<model("ecoworldpaginas.ecoworldpaginas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ecoworldpaginas.object', {
#             'object': obj
#         })