# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class MarquetingDigital(models.Model):
    _name = 'marqueting_digital.marqueting_digital'
    _description = 'Marqueting Digital'

    value = fields.Char(string='Subject')
    name = fields.Date(string='Date', default=fields.Date.today)
    value2 = fields.Char(string='Submitter', default="odoo13")
    value3 = fields.Many2one('marqueting_digital.mailing_list', string='Recipient')
    description = fields.Text(string='Description')


class Email(models.Model):
    _name = 'marqueting_digital.email'
    _description = 'Email'

    subject = fields.Char(string='Subject')
    content = fields.Text(string='Content')
    recipient = fields.Text(string='Recipient')  
    mailing_list_id = fields.Many2one('marqueting_digital.mailing_list', string='Mailing List')
    sender = fields.Char(string='Sender', default='odoo13')  

    date = fields.Date(string='Date')

    @api.model
    def create(self, vals):
        vals['sender'] = 'odoo13' 
        vals['date'] = fields.Date.today()
        return super(Email, self).create(vals)

    @api.onchange('mailing_list_id')
    def _onchange_mailing_list(self):
        if self.mailing_list_id:
            self.recipient = self.mailing_list_id


class MailingList(models.Model):
    _name = 'marqueting_digital.mailing_list'
    _description = 'Mailing List'

    name = fields.Char(string='Name')
    email_count = fields.Integer(string='Email Count', compute='_compute_email_count')
    emails = fields.One2many('marqueting_digital.email', 'mailing_list_id', string='Emails')

    @api.depends('emails')
    def _compute_email_count(self):
        for record in self:
            record.email_count = len(record.emails)
