'''
El siguiente programa sirve para gestionar los recursos de la conexion,
mas en especifico el cursor
'''
from Logger import log # importamos el logger
from Conexion import Conexion # importamos el pool
import sys


class CursorPool(object):
    #clase para gestionar los recursos del pool

    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        #Metodo para obtener el cursor
        log.info('Metodo __enter__ iniciado')
        self._conexion = Conexion().getConnection()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        #Metodo para hacer rollback, commit y salir de la conexion

        log.info('Metodo __exit__ iniciado')

        if exc_val:
            log.error(f'Ha ocurrido una excepcion {exc_type}: {exc_val} : {exc_tb}')
            self._conexion.rollback() # se ejecuta un rollback
            sys.exit()

        else:
            self._conexion.commit() # se hace commit de la transaccion
            log.info('Se ha realizado la transaccion con exito')

            self._cursor.close() #se cierra el cursor
            Conexion.freeConn(self._conexion) # se libera la conexion
            log.info(f'Se ha liberado la conexion {self._conexion}')

if __name__ == '__main__':
    #prueba del modulo
    with CursorPool() as cursor:
        cursor.execute("SELECT * FROM usuarios")
        print(cursor.fetchall())
