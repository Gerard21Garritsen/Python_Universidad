'''Crear una clase Padre que se creen objetos de tipo pelicula'''

class Peliculas:
    '''Clase para crear objetos de tipo pelicula'''

    #Inicializamos el constructor y sus variables de instacia
    def __init__(self, pelicula: str):
        self._pelicula = pelicula

    #definimos los metodos Get y Set para los atributos de instancia
    @property
    def pelicula(self):
        return self._pelicula

    @pelicula.setter
    def pelicula(self, pelicula):
        self._pelicula = pelicula

    #sobreescribimos el metodo str
    def __str__(self):
        return f'{self._pelicula}'
