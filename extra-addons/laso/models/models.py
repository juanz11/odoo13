# -*- coding: utf-8 -*-

from odoo import models, fields, api

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

  #   value = fields.Integer()
  #   value2 = fields.Float(compute="_value_pc", store=True)
     
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100