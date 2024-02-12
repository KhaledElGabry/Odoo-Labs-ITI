from odoo import models, fields

class Department(models.Model):
     _name = 'hms.department'
     
     name = fields.Char(string='Name')
     capacity = fields.Integer(string='Capacity')
     is_opened = fields.Boolean(string='Is Opened', default=True)
     patients = fields.One2many('hms.patient', 'department_id', string='Patients')
     