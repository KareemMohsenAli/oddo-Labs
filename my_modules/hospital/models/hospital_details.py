from odoo import models,fields

class Hospital(models.Model):
    _name="hospital.model"
    firstname=fields.Char()
    lastname=fields.Char()
    birthday=fields.Date()
    history=fields.Html()
    cr_ratio=fields.Float()
    blood_type=fields.Selection([('a+',"a+"),("b+","b+"),("c+","c+"),("o+","o+"),("a-","a-"),("b-","b-"),("c-","c-"),("o-","o-")])
    bcr=fields.Boolean()
    images=fields.Image()
    adress=fields.Text()
    age=fields.Integer()



    state = fields.Selection([ ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious')],string='State', default='undetermined')
    department_id=fields.Many2one('hms.department', string='Department')
    doctors_id=fields.Many2many('hms.doctors', string='Doctors')
    History=fields.Char(string='History')

