# -*- coding: utf-8 -*-
from odoo import http

# class GestionMairie(http.Controller):
#     @http.route('/gestion_mairie/gestion_mairie/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_mairie/gestion_mairie/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_mairie.listing', {
#             'root': '/gestion_mairie/gestion_mairie',
#             'objects': http.request.env['gestion_mairie.gestion_mairie'].search([]),
#         })

#     @http.route('/gestion_mairie/gestion_mairie/objects/<model("gestion_mairie.gestion_mairie"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_mairie.object', {
#             'object': obj
#         })