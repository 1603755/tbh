from odoo import models, fields

class Event(models.Model):
    _name = 'event.event'
    _description = 'Event Model'

    name = fields.Char(string='Evento')
    date_time = fields.Datetime(string='Fecha y hora de la boda/evento')
    location = fields.Char(string='Ubicación')
    comments = fields.Text(string='Comentarios')
    witness_1 = fields.Many2one('res.partner', string='Testigo 1')
    witness_2 = fields.Many2one('res.partner', string='Testigo 2')
    task = fields.Many2one(comodel_name='project.task',required=True)