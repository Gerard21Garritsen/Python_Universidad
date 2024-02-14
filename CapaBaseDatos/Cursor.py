#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Este archivo tiene la clase Cursor la cual es la encargada del
manejo de recursos de with
'''
from Logger import log # importamos log
from Conexion import Conexion

class Cursor(object):
    #Clase para el manejo del cursor con with
    
    def __init__(self):
        self._conexion = None
        self._cursor = None
    
    #definimos el metodo enter
    def __enter__(self):
        #obtenemos el cursor
        log.debug(f'Inicia el metodo __enter__')
        self._conexion = Conexion.getPool() # obtenemos la conexion
        self._cursor = self._conexion.cursor() # obtenemos el cursor
        
        return self._cursor
    
    #definimos el metodo exit
    def __exit__(self, tipo_exep, valor_exep, detalle_exep):
        log.debug('Inicia el metodo __exit__')
        
        if valor_exep:
            self._conexion.rollback() # se hace rolllback
            log.debug(f'Ocurrio un evento hacemos Rollback\n\r{tipo_exep} {valor_exep} {detalle_exep}')
            
        else:
            self._conexion.commit() # se hace commit
            log.debug('Se ejecuto el commit')
        
        self._cursor.close() # se cierra el cursor
        Conexion.freePool(self._conexion) # se libera la conexion
        
if __name__ == '__main__':
    #pruebas del modulo
    
    #creamos una conexion con with y hacemos una query
    with Cursor() as cursor:
        cursor.execute('SELECT * FROM Personas')
        registros = cursor.fetchall()

    log.debug(registros)