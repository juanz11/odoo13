# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

class Visit(models.Model):
    #atributos obligatorios del modelo
     _name = 'laso.visit'
     _description = 'Visit'
     
     #Los campos de un modelo se declaran como atributos del modelo... Un campo es representado
     #Como una columna en la base de datos
     
     name = fields.Char(string='Descripcion')
     #Se declara este atributo como relacional
     customer = fields.Many2one(string='Cliente' ,comodel_name='res.partner')
     date= fields.Datetime(string='Fecha')
     type = fields.Selection([('P', 'Presencial'), ('W','WhatsApp'),('T','telofonico')], string='Tipo', required=True)
     done = fields.Boolean(streing='Realizada', readonly=True)
     image= fields.Binary(string='Imagen')

    #Cambia el valor del atributo done
    #En python el objeto que referencia una instancia se identifica como self
     def toggle_state(self):
       self.done = not self.done

        #ORM
     def f_create(self):
        visit = {
            'name': 'ORM test',
            'customer': 1,
            'date': str(datetime.date(2021, 12, 10)),
            'type': 'P',
            'done': False
        } 
        print(visit)
        self.env['laso.visit'].create(visit)

     def f_search_update(self):
        visit = self.env['laso.visit'].search([('name', '=', 'ORM test')])
        print('search()', visit, visit.name)

        visit_b = self.env['laso.visit'].browse(visit[:1])
        print('browse()', visit_b, visit_b.name)

        visit.write({
            'name': 'ORM test write uhu'
        })

     def f_delete(self):
        visit = self.env['laso.visit'].browse([8])
        visit.unlink()

  #   value = fields.Integer()
  #   value2 = fields.Float(compute="_value_pc", store=True)
     
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100