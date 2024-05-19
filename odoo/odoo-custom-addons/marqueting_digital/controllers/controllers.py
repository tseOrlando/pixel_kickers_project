# -*- coding: utf-8 -*-
from odoo import http


class MarquetingDigital(http.Controller):
    @http.route('/marqueting_digital/marqueting_digital', auth='public')
    def index(self, **kw):
         return "Hello, world"

    @http.route('/marqueting_digital/marqueting_digital/objects', auth='public')
    def list(self, **kw):
         return http.request.render('marqueting_digital.listing', {
             'root': '/marqueting_digital/marqueting_digital',
             'objects': http.request.env['marqueting_digital.marqueting_digital'].search([]),
         })

    @http.route('/marqueting_digital/marqueting_digital/objects/<model("marqueting_digital.marqueting_digital"):obj>', auth='public')
    def object(self, obj, **kw):
         return http.request.render('marqueting_digital.object', {
             'object': obj
         })
