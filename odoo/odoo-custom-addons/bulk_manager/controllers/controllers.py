
from odoo import http


class BulkManager(http.Controller):
    @http.route('/bulk_manager/bulk_manager', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/bulk_manager/bulk_manager/objects', auth='public')
    def list(self, **kw):
        return http.request.render('bulk_manager.listing', {
            'root': '/bulk_manager/bulk_manager',
            'objects': http.request.env['bulk_manager.bulk_manager'].search([]),
        })

    @http.route('/bulk_manager/bulk_manager/objects/<model("bulk_manager.bulk_manager"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('bulk_manager.object', {
           'object': obj
         })