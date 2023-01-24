from odoo import models, fields



class SnehithModuleUsersTable(models.Model):
	_name = 'snehithmodule.userstable'	
	name = fields.Char('Title', required=True)	
	