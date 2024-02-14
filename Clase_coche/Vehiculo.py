#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Crear una clase Padre Vehiculo y dos clases hijas llamadas Coche y Bicicleta,
la clase padre debe detener los siguientes metodos y atributos:
    Atributos: color y ruedas
    Metodos: init y str
    
    La clase coche debe tener los atributos propios:
        Atributos: velocidad km/h
        Metodos: init y str
        
    La clase bicicleta debe tener los metodos y atributos:
        Atributos: tipo (urbana/montaña/etc)
        Metodos: init y str
'''
#Definimos la clase padre Vehiculo

class Vehiculo:
    
    #Inicializamos los atributos
    def __init__(self, color, ruedas):
        
        self._color = color
        self._ruedas = ruedas
    
    #creamos el metodo str
    def __str__(self):
        
        cadena = 'El color es: ' + self._color + ',' + 'Tiene ' + str(self._ruedas) + ' ruedas'
        return cadena
    
    #Establecemos los metodos Get y Set
    @property
    def color(self):
        return self._color
    @property
    def ruedas(self):
        return self._ruedas
    @color.setter
    def color(self, color):
        self._color = color
    @ruedas.setter
    def ruedas(self, ruedas):
        self._ruedas = ruedas

#Definimos la clase hija Coche

class Coche(Vehiculo):
    
    #Definimos el metodo init
    def __init__(self, color: str, ruedas: int, velocidad: int):
        super().__init__(color, ruedas)
        self._velocidad = velocidad
        
    #Definimos el metodo str
    def __str__(self):
        cadena = 'La velocidad es: ' + str(self._velocidad) + ' (km/h)'
        return f'{super().__str__()} {cadena}'
    
    #Definimos los metodos Get y Set
    @property
    def velocidad(self):
        return self._velocidad
    
    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad
    
    
#Definimos la clase hija bicicleta
class Bicicleta(Vehiculo):
    
    #definimos el metodo init
    def __init__(self, color: str, ruedas: int, tipo: str):
        super().__init__(color, ruedas)
        self._tipo = tipo
    
    #definimos el metodo str
    def __str__(self):
        cadena = 'La bicicleta es de ' + self._tipo
        return f'{super().__str__()} {cadena}'
    
    #definimos los metodos Get y Set
    
    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

#Definimos el codigo que se ejecuta si ejecutamos el archivo como principal
if __name__ == '__main__':
    
    print("Hola Hijos de la chingada")