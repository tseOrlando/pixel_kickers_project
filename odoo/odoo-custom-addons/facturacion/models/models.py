# -*- coding: utf-8 -*-
from odoo import models, fields, api

class VentasFacturas(models.Model):
    _name = 'ventas_facturas.ventas_facturas'
    _description = 'Facturas de Ventas'

    numero_factura = fields.Char(string="Invoice Number", required=True)
    cliente = fields.Many2one('res.partner', string="Customer", required=True)
    fecha_factura = fields.Date(string="Date", required=True)
    precio = fields.Float(string="Price", required=True)
    estado_factura = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('paid', 'Paid'),
        ('canceled', 'Canceled')
    ], string="Status", required=True, default='draft')

class Cliente(models.Model):
    _name = 'clientes.cliente'
    _description = 'Cliente'

    name = fields.Char(string='Name', required=True)
    last_name = fields.Char(string='Last Name')
    company_name = fields.Char(string='Nombre Emp')
    mobile = fields.Char(string='Phone')
    category_id = fields.Many2one('res.partner.category', string='Categoría')