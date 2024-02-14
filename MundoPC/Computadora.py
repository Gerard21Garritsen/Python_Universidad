'''Crear la clase Computadora que recibe objetos Raton, Teclado y Monitor'''

from TipoEntrada import Raton, Teclado, Monitor

class Computadora:

    Idcounter = 0 #Inicializamos el contador de computadoras

    def __init__(self, nombre, raton, teclado, monitor):
        Computadora.Idcounter += 1 #incrementamos el contador
        self._nombre = nombre
        self._raton = raton #Objeto Raton
        self._teclado = teclado #Objeto Teclado
        self._monitor = monitor #Objeto Monitor

    @property
    def nombre(self):
        return self._nombre
    @property
    def raton(self):
        return self._raton
    @property
    def teclado(self):
        return self._teclado
    @property
    def monitor(self):
        return self._monitor

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    @raton.setter
    def raton(self, raton):
        self._raton = str(raton)
    @teclado.setter
    def teclado(self, teclado):
        self._teclado = str(teclado)
    @monitor.setter
    def monitor(self, monitor):
        self._monitor = str(monitor)

    def __str__(self):
        return f'''La computadora {self._nombre}, esta compuesta de {self._raton}, {self._teclado}, {self._monitor}'''

if __name__ == '__main__':
    rat1 = Raton('usb', 'hp')
    print(rat1)
    tec1 = Teclado('rf', 'apple')
    print(tec1)
    monitor1 = Monitor('Samsung', '24 inches')
    print(monitor1)
    comp1 = Computadora(nombre='Pc', raton=rat1, teclado=tec1, monitor=monitor1)
    print(comp1)