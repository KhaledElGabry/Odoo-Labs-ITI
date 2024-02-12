from odoo import models, fields

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
     age = fields.Integer()
     long_history = fields.Text()
     status=fields.Selection([('undetermined', 'Undetermined'), ('good', 'Good'),('fair', 'Fair'),('serious', 'Serious')])
     department_id = fields.Many2one('hms.department', string='Departments')
     doctor_id = fields.Many2many('hms.doctor', string='Doctors')
     department_Capacity = fields.Integer(related='department_id.capacity', string='Departments Capacity', readonly=True)
     