'''Crear una clase Padre que reciba un objeto de tipo pelicula y que tenga los metodos:
- Agregar pelicula (static)
- Listar peliculas (static)
- Eliminar todo el archivo
Estos metodos deben operar sobre un arhivo'''

from Domain.Peliculas import Peliculas # importamos el modulo Peliculas
import os #importamos la libreria os para eliminar el arhivo

class Catalogo:
    '''Clase que recibe un objeto de tipo pelicula para agregarlo a un archivo'''

    #definimos una variable de clase
    ruta_archivo = 'peliculas.txt'

    #metodo para añadir peliculas
    @classmethod
    def add_pelicula(cls, nombre):
        #Agrega una pelicula al arhivo
        with open(cls.ruta_archivo, 'a', encoding='utf-8') as pelicula:
            pelicula.write(f'{nombre.pelicula}\n')

    #metodo para listar las peliculas agregadas
    @classmethod
    def listar_peliculas(cls):
        #Listar las peliculas
        with open(cls.ruta_archivo, 'r', encoding='utf-8') as pelicula:
            print("Catalogo de Peliculas".center(50, '-'))
            print(pelicula.read())

    #metodos para eliminar el archivo creado
    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print("Archivo eliminado".center(50))


if __name__ == '__main__':
    #Pruebas del modulo

    pel1 = Peliculas("Batman")
    print(pel1)
    Catalogo.add_pelicula(pel1)
    Catalogo.listar_peliculas()
