'''Este archivo crea una clase hija Cuadrado que hereda de
FigurasGeometricas y de Color, esta clase hija debe contener
los siguientes atributos/metodos:
un metodo que calcule el area de un cuadrado'''
from FigurasGeometricas import FigurasGeometricas
from Color import Color


class cuadrado(FigurasGeometricas, Color):
    def __init__(self, lado,  color):
        FigurasGeometricas.__init__(self, lado, lado)
        Color.__init__(self, color)

    def __str__(self):
        return f'El cuadrado tiene las dimensiones: {FigurasGeometricas.__str__(self)} y color: {Color.__str__(self)}'

    #definimos la funcion abstacta para calcular el area
    def area(self):
        return self.alto * self.ancho