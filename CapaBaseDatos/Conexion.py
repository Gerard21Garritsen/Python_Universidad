#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging as log # importamos la libreria logging
from psycopg2 import pool # importamos la libreria para el manejo de la BD
import sys            # importamos sys para salir del pograma

#definimos los parametros del logger
log.basicConfig(level=log.DEBUG, 
                    format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s', 
                    datefmt= '%I:%M:%S %p',
                    handlers= [log.FileHandler(filename='CapadeDatos.txt', encoding='utf-8', mode= 'w+'),
                               log.StreamHandler()])

class Conexion(object):
    #definimos las variables de clase para la conexion a la BD
    _HOST = '127.0.0.1'
    _PORT = '5432'
    _USER = 'gilbertgarritsen'
    _PASSWORD = 'root'
    _DBNAME = 'testpython'
    
    #definimos la variable para el pool
    _MINCONN = 0
    _MAXCONN = 2
    _pool = None
    
    #creamos el metodo de clase para la conexion
    @classmethod
    def poolConn(cls):
        
        if cls._pool is None:
            #creamos el pool
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MINCONN, cls._MAXCONN,
                host = cls._HOST, port = cls._PORT, user = cls._USER, password = cls._PASSWORD,
                dbname = cls._DBNAME)
                
                log.debug(f'Se ha creado el Pool con exito {cls._pool}')
                return cls._pool # retornamos el pool
            
            except Exception as e:
                log.error(f'Ha ocurrido un error al crear el Pool\n\r{e}')
                sys.exit()
            
        else:
            #si ya se creo el pool
            return cls._pool
    
    #creamos el metodo de clase para obtener el pool
    @classmethod
    def getPool(cls):
        conexion = cls.poolConn().getconn()
        log.debug(f'Se ha obtenido la conexion con exito {conexion}')
        
        return conexion
    
    #creamos la clase para liberar conexiones
    @classmethod
    def freePool(cls, conexion):
        cls.poolConn().putconn(conexion)
        log.debug(f'Se ha liberado la conexion {conexion}')
        
    #creamos la clase que cierre todas las conexiones
    @classmethod
    def closePool(cls):
        cls.poolConn().close()
        log.debug('Se ha cerrado el Pool')


if __name__ == '__main__':
    #probamos el modulo
    
    Conexion1 = Conexion.getPool()
    Conexion2 = Conexion.getPool()
    Conexion.freePool(Conexion1)
    Conexion3 = Conexion.getPool()
