from odoo import models, fields



class SHRUTHIModuleUsersTable(models.Model):
	_name = 'odoomodule.odootable'	
	name = fields.Char('Title', required=True)	
	