from odoo import http

class SnehithModule(http.Controller):

    @http.route('/snehith/website/', auth='public', website=True)
    def index(self, **kw):
        discforum = http.request.env['snehithmodule.discforum']
        return http.request.render('snehith_module.template_discforum', {
            'snehiths': discforum.search([])
        })
