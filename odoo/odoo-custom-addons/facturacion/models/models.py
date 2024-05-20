from odoo import models, fields, api

class FacturaCategoria(models.Model):
    _name = 'ventas_facturas.factura_categoria'
    _description = 'Invoice Category'

    name = fields.Char(string="Category Name", required=True)
    price = fields.Float(string="Price", required=True)

class VentasFacturas(models.Model):
    _name = 'ventas_facturas.ventas_facturas'
    _description = 'Sales Invoices'

    numero_factura = fields.Char(string="Invoice Number", required=True)
    cliente = fields.Many2one('clientes.cliente', string="Customer", required=True)
    fecha_factura = fields.Date(string="Invoice Date", required=True)
    precio = fields.Float(string="Price", required=True)
    estado_factura = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('paid', 'Paid'),
        ('canceled', 'Canceled')
    ], string="Invoice Status", required=True, default='draft')
    categoria_id = fields.Many2one('ventas_facturas.factura_categoria', string="Category", required=True)

    @api.onchange('categoria_id')
    def _onchange_categoria_id(self):
        if self.categoria_id:
            self.precio = self.categoria_id.price

class Cliente(models.Model):
    _name = 'clientes.cliente'
    _description = 'Customer'

    name = fields.Char(string='Name', required=True)
    last_name = fields.Char(string='Last Name')
    company_name = fields.Char(string='Company Name')
    mobile = fields.Char(string='Mobile Number')
    category_id = fields.Many2one('res.partner.category', string='Category')
