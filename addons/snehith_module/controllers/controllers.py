from odoo import http

class SnehithModule(http.Controller):

    @http.route('/snehith/website/', auth='public', website=True)
    def index(self, **kw):
        Userstable = http.request.env['snehithmodule.userstable']
        return http.request.render('snehith_module.index', {
            'snehiths': Userstable.search([])
        })
