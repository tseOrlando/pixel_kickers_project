# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MarquetingDigital(models.Model):
    _name = 'marqueting_digital.marqueting_digital'
    _description = 'Marqueting Digital'

    name = fields.Char(string='Holiwiiwiwiwiwaa')
    value = fields.Integer(string='Value')
    value2 = fields.Float(string='Value 2', compute="_value_pc", store=True)
    description = fields.Text(string='Description')

    email_ids = fields.One2many(comodel_name='marqueting_digital.email', inverse_name='marqueting_digital_id', string='Emails')

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

class Email(models.Model):
    _name = 'marqueting_digital.emaail'
    _description = 'Email'

    date = fields.Datetime(string='Date')
    subject = fields.Char(string='Subject')
    sender = fields.Char(string='Sender')
    content = fields.Text(string='Content')
    recipient = fields.Char(string='Recipient')
    marqueting_digital_id = fields.Many2one('marqueting_digital.marqueting_digital', string='Marqueting Digital')
