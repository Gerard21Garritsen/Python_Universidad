'''
El siguiente programa tiene un menu para realizar las cuatro operaciones basicas
en una BD (CRUD) (Create, Read, Update, and Delete)
'''

from UsuarioDAO import UsuarioDAO
from Usuario import Usuario


if __name__ == '__main__':
    #Inicio del menu

    opc = 0  # variable para obtener la opcion del menu
    val = True # variable para validar la entrada de solo digitos

    while opc != 5:
        #Menu

        opc = input('''Ingrese la operacion deseada: 
        \n\r1) Listar usuarios de la BD
        \n\r2) Agregar un nuevo usuario
        \n\r3) Actulizar un usuario
        \n\r4) Eliminar un usuario
        \n\r5) Salir: ''')

        #validar si la cadena contiene solo numeros
        val = opc.isdigit()

        if val:
            #Si se ha ingresado un valor valido
            opc = int(opc) # convertimos a entero

            if opc == 1:
                #Operacion Listar registros

                usuario = UsuarioDAO().readSQL()

                for usr in usuario:
                    print(usr)

            elif opc == 2:
                #Operacion Agregar un usuario

                nombre = None
                password = None

                cadena = input('Ingrese los datos del nuevo usuario separados por coma y espacio: ')
                lista = cadena.split(', ') # separamos la cadena

                nombre = lista[0]
                password = lista[1]

                usuario = Usuario(nombre=nombre, password=password)
                UsuarioDAO().insertSQL(usuario)

            elif opc == 3:
                #Operacion Actualizar un registro

                id_usr = 0
                nombre = None
                password = None

                id_usr = int(input('Ingresa el id del usuario a modificar: '))

                cadena = input('Ingrese los datos del usuario a modificar separados por coma y espacio: ')
                lista = cadena.split(', ')  # separamos la cadena
                nombre = lista[0]
                password = lista[1]

                usuario = Usuario(nombre=nombre, password=password, id_usuario=id_usr)
                UsuarioDAO().updateSQL(usuario)

            elif opc == 4:
                #Operacion Borrar un usuario

                id_usr = int(input('Ingrese el id del usuario a eliminar: '))

                UsuarioDAO().DeleteSQL(id_usr)
            else:
                print('Ingrese una opcion valida (1 - 5)')
        else:
            opc = 0 # reasignamos el valor

            print('Ingrese solo valores numericos')

print("\n\rSaliendo del programa...")