from odoo import models, fields, api
from odoo.exceptions import UserError


class customer(models.Model):
    _inherit = 'res.partner'
    related_patient_id = fields.Many2one('hospital.model')
    @api.constrains('related_patient_id')
    def _check_patient_mail(self):
        if self.email == self.related_patient_id.Email:
            raise UserError("Existing E-mail!")
    def unlink(self):
        if self.related_patient_id:
            raise UserError("You can't delete student")
        super().unlink()
