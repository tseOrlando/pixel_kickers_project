# -*- coding: utf-8 -*-
# from odoo import http


# class Calendario(http.Controller):
#     @http.route('/calendario/calendario', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/calendario/calendario/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('calendario.listing', {
#             'root': '/calendario/calendario',
#             'objects': http.request.env['calendario.calendario'].search([]),
#         })

#     @http.route('/calendario/calendario/objects/<model("calendario.calendario"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('calendario.object', {
#             'object': obj
#         })
