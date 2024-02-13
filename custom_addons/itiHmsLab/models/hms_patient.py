from odoo import models, fields, api
import re
from odoo.exceptions import UserError, ValidationError
from datetime import date

class Patient(models.Model):
     _name = 'hms.patient'
     _rec_name='firstName'
     
     firstName = fields.Char()
     lastName = fields.Char()
     birthDate = fields.Date()
     history = fields.Html()
     CRRatio = fields.Float()
     bloodType = fields.Selection([("A+", "A+"),("A-", "A-"),("B+","B+"),("B-","B-"),("O+","O+"),("O-","O-"),("AB+","AB+"),("AB-","AB-")])
     PCR = fields.Boolean()
     image = fields.Image(string="image", attachment=True, image=True)
     address = fields.Text()
     age = fields.Integer(compute='calculate_age' , store=True)
     long_history = fields.Text()
     status=fields.Selection([('undetermined', 'Undetermined'), ('good', 'Good'),('fair', 'Fair'),('serious', 'Serious')])
     department_id = fields.Many2one('hms.department', string='Departments')
     doctor_id = fields.Many2many('hms.doctor', string='Doctors')
     department_Capacity = fields.Integer(related='department_id.capacity', string='Departments Capacity', readonly=True)
     
     log_ids = fields.One2many('hms.log', 'patient_id', string='Log Record')
     description = fields.Text(related='log_ids.description', string='Description', readonly=True)
     email = fields.Char(required=True, string="Email")
     

     @api.constrains('email')
     def checkEmail(self):
        for rec in self:
            if rec.email:
                  if not re.match(r"^(([^<>()[\]\\.,;:\s@']+(\.[^<>()[\]\\.,;:\s@']+)*)|('.+'))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$", rec.email):
                     raise ValidationError("Invalid Email")
                  if self.env['hms.patient'].search_count([('email', '=', rec.email)]) > 1:
                    raise ValidationError("Email must be an unique")
                 
     _sql_constraints = [
        ('unique_patient_name','UNIQUE(firstName)','This Name is already exists')
     ]
    
     @api.onchange('status')
     def log_state(self):
        for rec in self:
            rec.env['hms.log'].create(
                {'description': 'Status Changed %s'%rec.status ,
                 'patient_id' : rec.id
                 }
            )    
    
     @api.depends('birthDate')
     def calculate_age(self):
         for rec in self :
            if rec.birthDate:
                today = date.today()
                rec.age = today.year - rec.birthDate.year - (
                    (today.month,today.day) <(rec.birthDate.month,rec.birthDate.day)
                )
            else:
                rec.age = 0
    
    
     @api.onchange('age')
     def setPCR (self):
        for rec in self:
            if rec.age < 30 :
                rec.PCR = True
            else:
                pass  
     @api.constrains('PCR')
     def check_PCR(self):
        for rec in self:
            if rec.age < 30 and not rec.PCR:
                raise UserError("The PCR is automatically checked if the age is lower than 30")
            
    
     
     