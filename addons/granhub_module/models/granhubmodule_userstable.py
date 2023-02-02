from odoo import models, fields, api



class GRANHUBModuleUsersTable(models.Model):
	_name = 'granhubmodule.userstable'	
	name = fields.Char('Title', required=True)	
	