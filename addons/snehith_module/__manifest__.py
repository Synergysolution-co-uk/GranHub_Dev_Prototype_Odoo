{
	'name': 'Snehith Module',
    'summary' : "Module to make granhub",
	'description' : """Shows List of Discussion Topic and detailed discussions""",
	'author' : "Synergy Solutions",
	'license' : "AGPL-3",
	'website' : "www.synergysolutions.co.uk",
	'category' : 'Uncategorized',
	'version' : '16.0.2.0.0',
	'depends' : ['website'],
	'data' : [
		     'security/groups.xml',
		     'views/snehithmodule_userstable.xml',
             'views/snehithmodule_discforum.xml',
	         'security/ir.model.access.csv',
             'views/template_topic.xml',
             'demo.xml'
             
	          ],	
}
