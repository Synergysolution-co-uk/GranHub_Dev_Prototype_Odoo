from odoo import models, fields

class SnehithModuleDiscforum(models.Model):
    _name = 'snehithmodule.discforum'
    name = fields.Char('Topic', required=True)
    description = fields.Char('Description', required=True)