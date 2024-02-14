'''
El presente archivo crea la clase Usuario
'''

from Logger import log # importamos el logger

class Usuario(object):
    '''clase para crear objetos de tipo usuario
    con id_usuario, nombre y password'''

    def __init__(self,nombre: str, password: str, id_usuario = 0):
        self._id_usuario = str(id_usuario) # convertimos todo a cadena
        self._nombre = str(nombre)
        self._password = str(password)

    #creamos los metodos Get y Set
    @property
    def id_usuario(self):
        return self._id_usuario

    @property
    def nombre(self):
        return self._nombre

    @property
    def password(self):
        return self._password

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = str(id_usuario)

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = str(nombre)

    @password.setter
    def password(self, password):
        self._password = str(password)

    def __str__(self):
        return f'Usuario [Id: {self._id_usuario} nombre: {self._nombre} psswd: {self._password}]'


if __name__ == '__main__':
    #prueba del modulo

    user = Usuario('Ernesto', 'ern123')
    log.info(user)