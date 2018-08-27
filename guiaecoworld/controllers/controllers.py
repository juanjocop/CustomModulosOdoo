# -*- coding: utf-8 -*-
from odoo import http

class Guiaeco(http.Controller):
    @http.route('/guiaecoworld', auth='public', website=True)
    def guiaeco(self, **kw):
        Clientes = http.request.env['guiaeco.clientes']
        return http.request.render('guiaecoworld.guiaecoworld_contenido',
            {'clientes4': Clientes.search([('activo', '=', True)], limit=4, order="fechaIncorporacion desc"),
            'clientes': Clientes.search([('activo', '=', True)], limit=100, order="name")})

    @http.route('/guiaecoworld/<int:lugar>', auth='public', website=True)
    def guiaecoprovincia(self, lugar, search, type, **kw):
        if type == 'provincia':
            Clientes = http.request.env['guiaeco.clientes']
            return http.request.render('guiaecoworld.guiaecoworld_contenido',
                {'clientes4': Clientes.search([('activo', '=', True), ('state_id', '=', lugar)], limit=4, order="fechaIncorporacion desc"),
                'provincia': search,
                'clientes': Clientes.search([('activo', '=', True), ('state_id', '=', lugar)], limit=100, order="name")})
        elif type == 'localidad':
            Clientes = http.request.env['guiaeco.clientes']
            return http.request.render('guiaecoworld.guiaecoworld_contenido',
                {'clientes4': Clientes.search([('activo', '=', True), ('city', '=', search)], limit=4, order="fechaIncorporacion desc"),
                'localidad': search,
                'clientes': Clientes.search([('activo', '=', True), ('city', '=', search)], limit=100, order="name")})
        elif type == 'nombre':
            Clientes = http.request.env['guiaeco.clientes']
            return http.request.render('guiaecoworld.guiaecoworld_contenido',
                {'clientes4': Clientes.search([('activo', '=', True), ('name', '=', search), ('id', '=', lugar)], limit=4, order="fechaIncorporacion desc"),
                'localidad': search,
                'clientes': Clientes.search([('activo', '=', True), ('name', '=', search), ('id', '=', lugar)], limit=100, order="name")})

    @http.route('/guiaecoworld/<model("guiaeco.clientes"):cliente>/', auth="public", website=True)
    def guiaecocliente(self, cliente, **kw):
        return http.request.render('guiaecoworld.ficha_cliente_guia', {'cliente': cliente})
