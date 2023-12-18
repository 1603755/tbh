from odoo import models, fields, api

class Task(models.Model):
    _inherit = 'project.task'
    
    expediente = fields.Many2one(comodel_name='proceedings.proceedings', domain="[('task','=',id)]")
    evento = fields.Many2one(comodel_name='event.event', domain="[('task','=',id)]")
    product = fields.Many2one(comodel_name='product.product',related='project_id.product_id')
    
    def write(self, vals):
        res = super(Task, self).write(vals)
        if res:
            self.expediente.task = self.id
            self.evento.task = self.id
        return res

    @api.model
    def create(self,vals):
        self.ensure_one()
        res = super(Task, self).create(vals)
        res.expediente.task = self.id
        res.evento.task = self.id
        return res