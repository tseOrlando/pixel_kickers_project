from odoo import models, fields

class BulkManagerGroups(models.Model):
    _name = 'bulk_manager.bulk_manager_groups'
    _description = 'bulk_manager.bulk_manager_groups'

    name = fields.Char(string='Name', required=True)
    product_ids = fields.One2many('bulk_manager.bulk_manager_product', 'bulk_group_id', string='Products')

class BulkManagerProduct(models.Model):
    _name = 'bulk_manager.bulk_manager_product'
    _description = 'bulk_manager.bulk_manager_product'

    name = fields.Char(string='Name', required=True)
    quantity = fields.Integer(string='Quantity', required=True)
    price = fields.Float(string='Price', required=True)
    currency_id = fields.Many2one(
        'res.currency', string='Currency',
        default=lambda self: self.env.ref('base.EUR').id
    )
    bulk_group_id = fields.Many2one(
        'bulk_manager.bulk_manager_groups', string='Bulk Group'
    )
