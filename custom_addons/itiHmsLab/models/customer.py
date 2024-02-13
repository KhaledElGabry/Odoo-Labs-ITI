from odoo import models, fields, api
from odoo.exceptions import ValidationError


class CustomersInherit(models.Model):
    _inherit = 'res.partner'
    
    patient_id = fields.Many2one('hms.patient', string='Patient')
    email = fields.Char(required=True)
    tax_id = fields.Char(required=True)



    @api.constrains('email')
    def check(self):
        
        for rec in self:
                if rec.email:
                    check_email = rec.env['hms.patient'].search([('email', '=', rec.email)], limit=1)
                if check_email:
                    raise ValidationError("This Email '%s' is already exists." % rec.email)
                
                if rec.patient_id:
                    check_patient = self.env['res.partner'].search([('patient_id', '=', rec.patient_id.id), ('id', '!=', rec.id)])
                if check_patient:
                    raise ValidationError("This patient is already linked")
