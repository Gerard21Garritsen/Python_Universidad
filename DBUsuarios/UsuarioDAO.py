'''
El presente programa crea la Clase UsuarioDAO, la cual sirve para
realizar las consultas a la DB y obtener los resultados, apoyandose
de los modulos previos para crear un objeto de tipo Usuario,
Conexion y gestion de los recursos (CursorPool)
'''
from Logger import log
from Usuario import Usuario
from CursorPool import CursorPool

class UsuarioDAO(object):
    #Clase usada para realizar consultas a la DB

    #definimos las operaciones a la base de datos
    _READ = 'SELECT * FROM usuarios GROUP BY id_usuario'
    _UPDATE = 'UPDATE usuarios SET nombre = %s, password = %s WHERE id_usuario = %s'
    _INSERT = 'INSERT INTO usuarios (nombre, password) VALUES (%s, %s)'
    _DELETE = 'DELETE FROM usuarios WHERE id_usuario = %s'

    @classmethod
    def readSQL(cls):
        #Metodo para leer los registros de la BD

        with CursorPool() as cursor:
            cursor.execute(cls._READ)
            registros = cursor.fetchall()
            reg = cursor.rowcount # recuperamos los registros leidos

            usuarios = []
            for registro in registros:
                usuarios.append(Usuario(id_usuario=registro[0], nombre=registro[1], password=registro[2]))

            log.info('Se han recuperado {registros} registros de la BD'.format(registros=reg))
            return usuarios # retornamos una lista de objetos Usuario

    @classmethod
    def insertSQL(cls, usuario):
        #Metodo para insertar un nuevo registro

        with CursorPool() as cursor:
            cursor.execute(cls._INSERT, (usuario.nombre, usuario.password))
            reg = cursor.rowcount
            return reg

    @classmethod
    def updateSQL(cls, usuario):
        #Metodo para actualizar un registro

        with CursorPool() as cursor:
            cursor.execute(cls._UPDATE, (usuario.nombre, usuario.password, usuario.id_usuario))
            reg = cursor.rowcount # obtenemos los registros afectados
            return reg

    @classmethod
    def DeleteSQL(cls, id_usuario):
        #Metodo para eliminar un registro

        with CursorPool() as cursor:
            cursor.execute(cls._DELETE, str(id_usuario))
            reg = cursor.rowcount # obtenemos los registros afectados
            return reg

if __name__ == '__main__':
    #prueba del modulo

    #prueba para agregar un nuevo usuario
    usuario1 = Usuario(nombre = 'Elliot', password= 'hello123')
    UsuarioDAO().insertSQL(usuario1)
