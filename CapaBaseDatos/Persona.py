#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Creamos la clase Persona para añadir nuevos registros a la DB

class Persona(object):
    
    #definimos los atributos de clase
    def __init__(self, nombre, apellido, id_persona = 0, email = 'email'):
        self._nombre = nombre
        self._apellido = apellido
        self._id_persona = id_persona
        self._email = email
    
    #creamos los metodos Get y Set
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @property
    def id_persona(self):
        return self._id_persona
    
    @property
    def email(self):
        return self._email
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
    
    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona
    
    @email.setter
    def email(self, email):
        self._email = email
    
    #definimos el metodo str
    def __str__(self):
        return f'''Persona[ID:{self._id_persona} nombre:{self._nombre} apellido:{self._apellido}
    email:{self._email}]'''

if __name__ == '__main__':
    #probamos el modulo
    
    people = Persona('Donovan', 'Sanchez', email='dsanchez@gmail.com')
    print(people)
    