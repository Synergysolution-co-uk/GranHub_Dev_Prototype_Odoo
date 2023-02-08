from odoo import http

class SnehithModule(http.Controller):

    @http.route('/snehith/website/', auth='public', website=True)
    def index(self, **kw):
        DiscForum= http.request.env['snehithmodule.discforum']
        return http.request.render('snehith_module.index', {
            'snehiths': DiscForum.search([])
        })
