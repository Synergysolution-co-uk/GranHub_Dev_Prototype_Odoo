from odoo import http

class SHRUTHI_Module(http.Controller):

    @http.route('/Granhubpage/Granhubpage/', auth='public')
    def index(self, **kw):
        return "Hello, world"