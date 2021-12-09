# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Visit(models.Model):
     _name = 'laso.visit'
     _description = 'Visit'
     
     name = fields.Char(string='Descripcion')
     customer = fields.Char(string='Cliente')
     date= fields.Datetime(string='Fecha')
     type = fields.Selection([('P', 'Presencial'), ('W','WhatsApp'),('T','telofonico')], string='Tipo', required=True)
     done = fields.Boolean(streing='Realizada', readonly=True)

  #   value = fields.Integer()
  #   value2 = fields.Float(compute="_value_pc", store=True)
     
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100