from odoo import models, fields

class Lead(models.Model):
    _inherit = "crm.lead"
    
    boda_fecha = fields.Date(string="¿Cuándo te quieres casar?")
    boda_lugar = fields.Char(string="¿Dónde te quieres casar?")
    