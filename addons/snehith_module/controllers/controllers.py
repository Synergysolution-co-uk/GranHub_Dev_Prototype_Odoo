from odoo import http

class SnehithModule(http.Controller):

    @http.route('/snehith/website/', auth='public', website=True)
    def index(self, **kw):
        discforum = http.request.env['snehithmodule.discforum']
        return http.request.render('snehith_module.template_discforum', {
            'snehiths': discforum.search([])
        })
from odoo import http

class SnehithModuleList(http.Controller):

    @http.route('/snehith/mainpage/', auth='public', website=True)
    def index(self, **kw):
        discforum = http.request.env['snehithmodule.discforum']
        return http.request.render('snehith_module.template_discforum_topic', {
            'snehiths': discforum.search([])
        })
    
class SnehithModuleTopic(http.Controller):

    @http.route('/snehith/topic/<model("snehithmodule.discforum"):webpage>/', auth='public', website=True)
    def topic_page(self, webpage):
        return http.request.render('snehith_module.template_topic', {
           'snehiths': webpage 
        })    