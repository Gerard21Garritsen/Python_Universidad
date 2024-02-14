'''
El siguiente archivo contiene la clase Conexion la cual es la encargada de iniciar la
conexion con la DB.
Tambien contiene la clase GetPool para obtener el pool,
la clase FreePool para liberar el pool,
la clase ClosePoll para cerrar todos los pool de conexiones
'''
from Logger import log # importamos el logger
from psycopg2 import pool # impotamos el modulo pool
import sys

class Conexion(object):
    '''La presente clase crea la conexion con la DB'''

    #definimos las variables de clase para la conexion a la DB
    _HOST = 'localhost'
    _PORT = '5432'
    _USER = 'gilbertgarritsen'
    _PASSWORD = ''
    _DBNAME = 'testpython'

    #definimos las variable de clase para la conexion al pool
    _MIN_POOL_SIZE = 0
    _MAX_POOL_SIZE = 2
    _poolconn = None

    @classmethod
    def connection(cls):
        #Creamos la conexion al pool
       if cls._poolconn is None:
           try:
               cls._poolconn = pool.SimpleConnectionPool(minconn=cls._MIN_POOL_SIZE, maxconn=cls._MAX_POOL_SIZE,
                                                         host=cls._HOST, port=cls._PORT, user=cls._USER,
                                                         password=cls._PASSWORD, database=cls._DBNAME)
               log.info(f'Se ha creado el pool con exito {cls._poolconn}')
               return cls._poolconn

           except Exception as e:
               log.error(f'Ha ocurrido un erro al crear el pool {e}')
               sys.exit()
       else:
           log.info(f'Ya existe un pool creado {cls._poolconn}')
           return cls._poolconn

    @classmethod
    def getConnection(cls):
        #Esta funcion obtiene una conexion del pool
        conexion = cls.connection().getconn() # la variable conexion debe ser local para dar nuevas conexiones
        log.info(f'Se ha obtenido la conexion exitosamente {conexion}')
        return conexion

    @classmethod
    def freeConn(cls, conexion):
        #Metodo para liberar la conexion
        cls.connection().putconn(conexion)
        log.info('Se ha liberado la conexion exitosamente')

    @classmethod
    def closeConn(cls):
        #Metodo para cerrar todas las conexiones al Pool
        cls.connection().close()
        log.info('Se han cerrado todas las conexiones exitosamente')


if __name__ == '__main__':
    #prueba del modulo
    
    conexion1 = Conexion().getConnection()
    conexion2 = Conexion().getConnection()
    conexion3 = Conexion().getConnection()