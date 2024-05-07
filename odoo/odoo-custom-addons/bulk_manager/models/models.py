# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo import api, exceptions, fields, models, SUPERUSER_ID

class bulk_manager_groups(models.Model):
    _name = 'bulk_manager.bulk_manager_groups'
    _description = 'bulk_manager.bulk_manager_groups'

    name = fields.Char(string='Name', required=True)
    
class bulk_manager(models.Model):
    _name = 'bulk_manager.bulk_manager'
    _description = 'bulk_manager.bulk_manager'

    name = fields.Char(string='Name')
    quantity = fields.Integer(string='Quantity', required=True)
    price = fields.Monetary(string='Price', currency='EUR')
    group = fields.Many2one('bulk_manager.bulk_manager_groups', string='Group')