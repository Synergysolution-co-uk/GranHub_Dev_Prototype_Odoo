from odoo import http

class SnehithModule(http.Controller):

    @http.route('/snehith/website/', auth='public')
    def index(self, **kw):
        return http.request.render('snehith.index', {
            'snehith': ["xxxxxxx", "yyyyyyyyy", "zzzzzzz"],
        })
