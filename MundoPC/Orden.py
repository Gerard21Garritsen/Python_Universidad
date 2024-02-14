'''Crear la clase Orden'''

#importamos las clases creadas
from Computadora import Computadora
from TipoEntrada import Raton, Teclado, Monitor

class Orden:

    Idcounter = 0 #inicializamos el contador de ordenes

    #inicializamos los atributos de instancia
    def __init__(self, ordenes):
        Orden.Idcounter += 1 #incrementamos el contador
        self._Orden = ordenes

    #metodo de instancia para agregar una nueva orden
    def addOrder(self, orden: list):
        Orden.Idcounter += 1
        self._Orden.append(orden)

    #definimos el metodo str
    def __str__(self):
        cadena = ''

        for orden in self._Orden:
            cadena += str(orden)
        return f'La orden {Orden.Idcounter} contiene:\n\r{cadena}\n\r'

if __name__ == '__main__':
    print("Prueba del programa")

    rat1 = Raton('usb', 'hp')
    print(rat1)
    tec1 = Teclado('rf', 'apple')
    print(tec1)
    monitor1 = Monitor('Samsung', '24 inches')
    print(monitor1)
    comp1 = Computadora(nombre='Pc', raton=rat1, teclado=tec1, monitor=monitor1)
    print(comp1)
    orden = [comp1]
    orden1 = Orden(orden)
    print(orden1)
