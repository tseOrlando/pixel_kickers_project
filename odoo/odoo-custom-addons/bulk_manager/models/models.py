# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo import api, fields, models, SUPERUSER_ID

class bulk_manager_groups(models.Model):
    _name = 'bulk_manager.bulk_manager_groups'
    _description = 'bulk_manager.bulk_manager_groups'

    name = fields.Char(string='Name', required=True)
    
class bulk_manager(models.Model):
    _name = 'bulk_manager.bulk_manager'
    _description = 'bulk_manager.bulk_manager'

    name = fields.Char(string='Name')
    quantity = fields.Integer(string='Quantity', required=True)
    price = fields.Integer(string='Price', currency_field='currency_id', required=True)
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.ref('base.EUR').id)
    bulk_group = fields.Many2one('bulk_manager.bulk_manager_groups', string='Bulk Group')