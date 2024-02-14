'''Crear una clase FiguraGeometrica que tenga como atributos:
Alto y Ancho
Estos atributos deben estar encapsulados
'''

from abc import ABC, abstractmethod

class FigurasGeometricas(ABC):
    def __init__(self, alto, ancho):
        if self._validar(alto):
            self._alto = alto
        else:
            self._alto = 0
        if self._validar(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print("Dimension no permitida")

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar(alto):
            self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar(ancho):
            self._ancho = ancho

    #Definimos el metodo str
    def __str__(self):
        cadena = "Alto (cm): " + str(self._alto) + " Ancho (cm): " + str(self._ancho)
        return cadena

    #definimos la funcion de validacion
    def _validar(self, dimension):
        return True if 0 < dimension < 15 else False

    #definimos el metodo abstracto para calcular el area de una figura
    @abstractmethod
    def area(self):
        pass