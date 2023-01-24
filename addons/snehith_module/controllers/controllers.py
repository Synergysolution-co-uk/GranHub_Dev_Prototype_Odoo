from odoo import http

class SnehithModule(http.Controller):

    @http.route('/snehith/website/', auth='public')
    def index(self, **kw):
        return "Hello, world"
