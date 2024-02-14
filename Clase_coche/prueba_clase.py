#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Codigo de prueba de la clase Vehiculo y sus hijos

from Vehiculo import *

#cremaos los objetos

vehiculo1 = Vehiculo("verde", 4)

coche1 = Coche("gris", 4, 65)

bicicleta1 = Bicicleta("naranja", 2, "montaña")

#probamos el contenido de los objetos

print(coche1)

print(bicicleta1)

coche1.color = "amarillo" #modificamos un atributo usando el metodo Get

print(coche1)
