'''Crear una clase hija Rectangulo que derive de las clases
FigurasGeometricas y color, esta clase hija debe tener un metodo que
calcule el area de un rectangulo'''
from FigurasGeometricas import FigurasGeometricas
from Color import Color

class rectangulo(FigurasGeometricas, Color):
    def __init__(self, alto, ancho, color):
        FigurasGeometricas.__init__(self, alto, ancho)
        Color.__init__(self, color)

    def __str__(self):
        return f'El rectangulo tiene dimensiones: {FigurasGeometricas.__str__(self)} y color: {Color.__str__(self)}'

    #definimos la funcion abstracta para calcular el area
    def area(self):
        return self.ancho * self.alto