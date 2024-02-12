from odoo import models, fields

class Doctor(models.Model):
     _name = 'hms.doctor'
     
     firstName = fields.Char()
     lastName = fields.Char()
     image=fields.Binary(string="image",attachment=True,image=True)
     patient_id = fields.Many2many('hms.patient', string='Patients')

     