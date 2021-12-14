# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


class Visit(models.Model):     #a estas clases se le define dos atributos nombre del modulo  y nombre del modelo visit en este caso
    _name = 'custom_crm.visit'
    _description = 'Visit'

    name = fields.Char(string='Descripción')  # los atributos de este campo la descripcion 
    customer = fields.Many2one(string='Cliente', comodel_name='res.partner') # customer el Many2one n visitas asociadas al cliente
    date = fields.Datetime(string='Fecha') # fecha que la llamamos date y vamos a ponerla cfomo un datetime el date almacena la fecha y el datetime fechy y hora
    type = fields.Selection([('P', 'Presencial'), ('W', 'WhatsApp'), ('T', 'Telefónico')], string='Tipo', required=True) #campo seleccion un despegable donde tenemos multiples opciones el tipo si la visita presencial o contacto celu añadiendo requeir true
    done = fields.Boolean(string='Realizada', readonly=True) #campo realizada valor boleano tru o false realizada 
    image = fields.Binary(string='Imagen')

    def toggle_state(self):
        self.done = not self.done 

    #ORM
    def f_create(self):
        visit = {
            'name': 'ORM juan',
            'customer': 1,
            'date': str(datetime.date(2021, 12, 14)),
            'type': 'P',  #tipo presencial
            'done': False #tipo si esta realiazada
        }
        print(visit)
        self.env['custom_crm.visit'].create(visit)  
#busqueda  el metodo seach le pasamos un array de duplas 
    def f_search_update(self):
        visit = self.env['custom_crm.visit'].search([('name', '=', 'ORM juan')])
        #print('search()', visit, visit.name)

      #  visit_b = self.env['custom_crm.visit'].browse([])
       # print('browse()', visit_b, visit_b.name)

     #   visit.write({
      #      'name': 'ORM test write'
       # })

        for v in visit:
           v.write({'name': 'ORM test write uhu'})

    def f_delete(self):
            visit = self.env['custom_crm.visit'].search([('name', '=', 'ORM test write uhu')])
            visit.unlink()

class VisitReport(models.AbstractModel): #va ederada de abstract model que se utliza para ederar otras clases y funcionalidad

    _name='report.custom_crm.report_visit_card' #mism nmombre que definimos en el visit name 

    @api.model                                          #invoque una funcion anotacion @api
    def _get_report_values(self, docids, data=None):         #definicion de la fucion recibe el self 
        report_obj = self.env['ir.actions.report']            
        report = report_obj._get_report_from_name('custom_crm.report_visit_card') #definir el report el nombre de visit  del formulario
        return {                     #return un dicionario
            'doc_ids': docids,
            'doc_model': self.env['custom_crm.visit'],   #nombre del modelo
            'docs': self.env['custom_crm.visit'].browse(docids)  #pasarle el atributo de las plantilla
        }


class CustomSaleOrder(models.Model):

    _inherit = 'sale.order'

    zone = fields.Selection([('N', 'Norte'), ('C', 'Centro'), ('S', 'Sur')], string='Zona comercial')