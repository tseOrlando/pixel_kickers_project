# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MarquetingDigital(models.Model):
    _name = 'marqueting_digital.marqueting_digital'
    _description = 'Marqueting Digital'

    name = fields.Date(string='Date', default=fields.Date.today)
    value = fields.Char(string='Subject')
    value2 = fields.Char(string='Submiter')
    value3 = fields.Char(string='Recipient')
    description = fields.Text(string='Description')


class Email(models.Model):
    _name = 'marqueting_digital.email'
    _description = 'Email'

    date = fields.Datetime(string='Date')
    subject = fields.Char(string='Subject')
    sender = fields.Char(string='Sender')
    content = fields.Text(string='Content')
    recipient = fields.Char(string='Recipient')
    marqueting_digital_id = fields.Many2one('marqueting_digital.marqueting_digital', string='Marqueting Digital')
    mailing_list_id = fields.Many2one('marqueting_digital.mailing_list', string='Mailing List')


class MailingList(models.Model):
    _name = 'marqueting_digital.mailing_list'
    _description = 'Mailing List'

    name = fields.Char(string='Name')
    email_count = fields.Integer(string='Email Count', compute='_compute_email_count')
    emails = fields.One2many('marqueting_digital.email', 'mailing_list_id', string='Emails')
    marqueting_digital_id = fields.Many2one('marqueting_digital.marqueting_digital', string='Marqueting Digital')

    @api.depends('emails')
    def _compute_email_count(self):
        for record in self:
            record.email_count = len(record.emails)
