# models/employee.py
from odoo import models, fields

class Employee(models.Model):
    _name = 'employee.management'
    _description = 'Employee Management'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    job_title = fields.Char(string='Job Title')
    department = fields.Char(string='Department')
    image = fields.Binary(string='Image')