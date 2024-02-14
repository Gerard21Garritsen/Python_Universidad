'''Creamos la clase Padre TipoEntrada'''

class DispositivoEntrada:
    def __init__(self, tipoentrada, marca):
        self._tipoentrada = tipoentrada
        self._marca = marca

    @property
    def tipoentrada(self):
        return self._tipoentrada
    @property
    def marca(self):
        return self._marca
    @tipoentrada.setter
    def tipoentrada(self, tipoentrada):
        self._tipoentrada = tipoentrada
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    def __str__(self):
        return f'Tipo entrada:{self._tipoentrada}, marca:{self._marca}'

#Definimos la clase Hija Raton
class Raton(DispositivoEntrada):

    Idcounter = 0 #creamos el contador global

    def __init__(self, tipoentrada, marca):
        super().__init__(tipoentrada, marca)
        Raton.Idcounter += 1 #incrementamos el contador
        self._idcontador = Raton.Idcounter

    @property
    def idcontador(self):
        return self._idcontador

    def __str__(self):
        return f'Raton[{super().__str__()}]'

#Definimos la clase Hija Teclado
class Teclado(DispositivoEntrada):

    Idcounter = 0 #contador dispositivos

    def __init__(self, tipoentrada, marca):
        super().__init__(tipoentrada, marca)
        Teclado.Idcounter += 1 #incrementamos al crear un objeto
        self._idcontador = Teclado.Idcounter

    @property
    def idcontador(self):
        return self._idcontador

    def __str__(self):
        return f'Teclado[{super().__str__()}]'

#Definimos la clase Hija Monitor
class Monitor(DispositivoEntrada):

    Idcounter = 0 #inicializamos el contador de productos

    def __init__(self,marca, tamaño):
        super().__init__(None, marca)
        Monitor.Idcounter += 1  # incrementamos el contador
        self._marca = marca
        self._tamaño = tamaño
        self._idcontador = Monitor.Idcounter

    @property
    def idcontador(self):
        return self._idcontador

    def __str__(self):
        return f'Monitor[Marca:{self._marca}, tamaño:{self._tamaño}]'

if __name__ == '__main__':
    pantalla = Monitor('Hp', '24 inches')
    print(pantalla)
    print(pantalla.idcontador)