from odoo import models, fields



class GRANHUBModuleUsersTable(models.Model):
	_name = 'granhubmodule.userstable'	
	name = fields.Char('Title', required=True)	
	