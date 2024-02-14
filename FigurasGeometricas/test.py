'''Archivo de prueba de las clases'''
from Cuadrado import cuadrado
from Rectangulo import rectangulo

#cremos los objetos
square = cuadrado(12, "gris")
rectangle = rectangulo(5, 10, "verde")

#imprimnimos sus propiedades
print(f'{square} \n\r{rectangle}')

#obtenemos el area del cuadrado y rectangulo
print(f"El area del cuadrado es: {square.area()} m2")

print(f"El area del rectangulo es: {rectangle.area()} m2")