#El siguiene codigo elimina uno o varios registros de la DB

import psycopg2

conexion = psycopg2.connect(host = 'localhost', database = 'testpython', user = 'postgres', password = '', port = '5432')

#iniciamos el proceso de consultas
with conexion:
    with conexion.cursor() as cursor:
        sql = "DELETE FROM Personas WHERE id_personas = %s"
        id = input("Introduce el id a eliminar: ")
        cursor.execute(sql, id)

        reg = cursor.rowcount #obtenemos el numero de registros a eliminar
        print(f'Se eliminaron {reg} registros')

conexion.close()
