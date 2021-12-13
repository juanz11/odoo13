# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions
import base64, io #se importan dos librerias propias de python

class CustomItem(models.Model):
    _name = 'odoo_view_advanced.custom_item'

    name = fields.Char(string='Descripción')
    unit_price = fields.Char(string='Precio unitario')

    def remove_items(self, user):
        print('Borrando items...')
        return True


#este modelo procesa la subida de archivos y se define como un modelo Transient
class UploadFile(models.TransientModel):
    _name = 'odoo_view_advanced.upload_file'

    #Estos dos campos se agregan a la vista del formulario
    upload_file = fields.Binary(string='Subir fichero', required=True)
    file_name = fields.Char(string='Nombre del fichero')

    #Si no se cancela la subida se ejecuta esta funcion
    #
    def import_file(self):
        if self.file_name:
            #La condicion verifica que en el nombre del archivo se especifique extension .csv
            #Si no es un .csv lanza una excepcion
            if '.csv' not in self.file_name:
                raise exceptions.ValidationError('El archivo debe ser un CSV')
            #Si es un archivo .csv lee el archivo
            #Crea un arreglo donde cada elemento es una linea
            file = self.read_file_from_binary(self.upload_file)
            lines = file.split('\n')
            #Cada linea es un registro y cada campo esta separado por ; si consigue almenos un campo
            #agrega el registro, conociendo la estructura del archivo, el primer campo es el nombre
            #el segundo es el precio unitario, que debe convertirse de cadena flotante a numero flotante
            for line in lines:
                elements = line.split(';')
                if len(elements) > 1:
                    self.env['odoo_view_advanced.custom_item'].create({
                        'name': elements[0],
                        'unit_price': float(elements[1])
                    })

    #cuando quiero inyectar el objeto self lo paso como primer parametro y en la llamada del metodo
    #no necesito pasar el self como parametro
    def read_file_from_binary(self, file):
        #intentamos 
        try:
            with io.BytesIO(base64.b64decode(file)) as f:
                f.seek(0)
                return f.read().decode('UTF-8')
        #si el archivo esta corrupto ejecutamos una excepcion e imprimimos en terminal el mensaje de error
        #levantamos una excepcion y finalizamos la ejecucion del programa
        except Exception as e:
            print(str(e))
            raise e










