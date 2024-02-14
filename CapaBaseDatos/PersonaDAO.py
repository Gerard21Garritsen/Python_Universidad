#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Vamos a crear la clase PersonaDAO la cual hara uso de la clase Persona y Conexion para
insertar nuevos registros a la BD. Las operaciones a realizar son CRUD (Create-Read-Update-Delete)
'''
from Logger import log        # importamos el log que hemos construido
from Persona import *         # importamos la clase Persona
from Conexion import *        # importamos la clase Conexion
from Cursor import *          # importamos la clase Cursor

class PersonaDAO(object):
    
    #definimos las operaciones a realizar como constantes
    _READ = 'SELECT * FROM Personas ORDER BY id_personas'
    _INSERT = 'INSERT INTO Personas (nombre, apellido, email) VALUES(%s, %s, %s)'
    _UPDATE = 'UPDATE Personas SET nombre=%s, apellido=%s, email=%s WHERE id_personas = %s'
    _DELETE = 'DELETE FROM Personas WHERE id_personas = %s'
    
    #definimos el metodo de clase read
    @classmethod
    def read(cls):
        #creamos la conexion
        with Cursor() as cursor:
            cursor.execute(cls._READ) #realizamos la consulta
            registros = cursor.fetchall() # recuperamos los registros
            
            personas = [] # lista que almacenara los objetos
            for valor in registros:
                person = Persona(id_persona= valor[0], nombre= valor[1],
                                        apellido= valor[2], email= valor[3])
                personas.append(person) # agregamos a la lista cada persona creada
            
            return personas #devolvemos los registros leidos
    
    #definimos el metodo de clase insert
    @classmethod
    def insert(cls, persona):
        #creamos la conexion
        with Cursor() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email) #obtenemos la tupla de valores
            cursor.execute(cls._INSERT, valores) # ejecutamos la query
            log.debug(f'Se ha agregado la persona {persona}')
            return cursor.rowcount # retornamos el numero de id añadido
    
    #definimos el metodo de clase update
    @classmethod
    def update(cls, persona):
        #creamos la conexion
        with Cursor() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email
                       , persona.id_persona)
            cursor.execute(cls._UPDATE, valores)
            
            #imprimimos el registro modificado
            log.debug(f'Se modifico el registro {persona.id_persona}, con el nuevo registro {persona}')
            return cursor.rowcount

    #definimos el metodo de clase DELETE
    @classmethod
    def delete(cls, id_del: int):
        #creamos la conexion
        with Cursor() as cursor:
            cursor.execute(cls._DELETE, (str(id_del),)) #ejecutamos la query
            
            log.debug(f'Se elimino el registro {id_del}')
            return cursor.rowcount


if __name__ == '__main__':
    #probamos el modulo
    
    #Leer los registros de la tabla
    '''reg = PersonaDAO.read()
    
    for registros in reg:
        print(registros)'''
    
    #inserta un nuevo registro en la tabla
    
    '''person = Persona(nombre='Estevan', apellido='Aranda', email='earanda@yahoo.com')
    registro = PersonaDAO.insert(person)
    log.debug(f'registro agregado {registro}')'''
    
    #se actualiza un registro
    '''person = Persona(nombre='Ariel', apellido='Vanean', email='avanean@bing.com', id_persona=3)
    registro = PersonaDAO.update(person)
    log.info(f'registro agregado {registro}')'''
    
    #se elimina un registro
    registro = PersonaDAO.delete(1)
    log.info(f'Registros afectados {registro}')
