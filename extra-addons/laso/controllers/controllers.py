# -*- coding: utf-8 -*-
from odoo import http

# class Laso(http.Controller):
#     @http.route('/laso/laso/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/laso/laso/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('laso.listing', {
#             'root': '/laso/laso',
#             'objects': http.request.env['laso.laso'].search([]),
#         })

#     @http.route('/laso/laso/objects/<model("laso.laso"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('laso.object', {
#             'object': obj
#         })