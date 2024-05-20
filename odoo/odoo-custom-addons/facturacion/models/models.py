# -*- coding: utf-8 -*-

from odoo import models, fields, api

class FacturacionVentaEntradas(models.Model):
    _name = 'facturacion_venta_entradas.facturacion_venta_entradas'
    _description = 'Facturacion Venta Entradas'

    factura_numero = fields.Char(string="Número de Factura")
    cliente_id = fields.Many2one('res.partner', string="Cliente")
    fecha_factura = fields.Date(string="Fecha de Factura")
    total_euros = fields.Float(string="Total en Euros")
    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('pagada', 'Pagada'),
        ('cancelada', 'Cancelada')
    ], string="Estado", default='borrador')
