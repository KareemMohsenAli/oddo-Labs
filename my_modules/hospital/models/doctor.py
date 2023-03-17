from odoo import models, fields

class Doctors(models.Model):
    _name='doctors.model'
    firstname=fields.Char()
    lastname=fields.Char()
    images=fields.Image()