from odoo import models, fields

class Proceedings(models.Model):
    _name = 'proceedings.proceedings'
    _description = 'Proceedings Model'

    TYPE_SELECTION = [
        ('notarial', 'Notarial'),
        ('registro_civil', 'Registro Civil')
    ]

    type = fields.Selection(TYPE_SELECTION, string='Tipo')
    expediente = fields.Char(string='Nº de expediente')
    comentarios = fields.Text(string='Comentarios')

    
    event_id = fields.Many2one('event.event', string='Evento')
    
    # Fields for "notarial" type
    notaria = fields.Many2one('res.partner', string='Notaria', domain="[('is_company','=',True)]", attrs={'invisible': [('type', '!=', 'notarial')]} )
    oficial_notaria = fields.Many2one('res.partner', string='Oficial de notaría', attrs={'invisible': [('type', '!=', 'notarial')]} )
    documentacion_solicitada = fields.Text(string='Documentación solicitada por el notario', attrs={'invisible': [('type', '!=', 'notarial')]} )
    documentacion_enviada = fields.Text(string='Documentación enviada', attrs={'invisible': [('type', '!=', 'notarial')]} )
    fecha_expediente = fields.Date(string='Fecha del expediente', attrs={'invisible': [('type', '!=', 'notarial')]} )

    # Fields for "registro_civil" type
    registro_civil_juzgado = fields.Many2one('res.partner', string='Registro Civil o juzgado', domain="[('is_company','=',True)]", attrs={'invisible': [('type', '!=', 'registro_civil')]} )
    documentacion_entregada = fields.Boolean(string='¿Han entregado la documentación antes de tener la cita?', attrs={'invisible': [('type', '!=', 'registro_civil')]} )
    cita_expediente_reservada = fields.Boolean(string='¿Hay cita reservada de expediente?', attrs={'invisible': [('type', '!=', 'registro_civil')]} )
    cita_boda_reservada = fields.Boolean(string='¿Hay cita reservada de boda?', attrs={'invisible': [('type', '!=', 'registro_civil')]} )
    task = fields.Many2one(comodel_name='project.task',required=True)
    
    def name_get(self):
        result = []
        for record in self:
            result.append((record.id,record.expediente))
        return result