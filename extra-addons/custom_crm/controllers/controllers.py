# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
import json


class VisitController(http.Controller):

    @http.route('/api/visits', auth='public', method=['GET'], csrf=False) #le pasamos la ruta donde quiere que responda nuestro metodo authoticacion la dejamos publica paero no es recomendado 
    def get_visits(self, **kw):        # el atributo csrf 
        try:
            visits = http.request.env['custom_crm.visit'].sudo().search_read([], ['id', 'name', 'customer', 'done']) #esta variante search read recibe dos parametros un array de duplas los campos que queremos recuperar 
            res = json.dumps(visits, ensure_ascii=False).encode('utf-8') # funcion dumps tranformar ese objeto en una estructura js para poder enviarla le pasamos el dicionario  
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:   #la expecion 
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)

