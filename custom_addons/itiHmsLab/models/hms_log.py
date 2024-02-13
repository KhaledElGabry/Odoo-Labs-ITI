from odoo import models,fields

class HmsLog(models.Model):
    _name = 'hms.log'
    
    patient_id = fields.Many2one('hms.patient', string='Patient')
    description = fields.Text(string='Description')
    
    