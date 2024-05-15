from odoo import models, fields

class CalendarioEvento(models.Model):
    _name = 'calendario.evento'
    _description = 'Evento de Calendario'

    name = fields.Char(string='Nombre del Evento', required=True)
    start_date = fields.Datetime(string='Fecha de Inicio', required=True)
    end_date = fields.Datetime(string='Fecha de Finalización', required=True)
    description = fields.Text(string='Descripción')
