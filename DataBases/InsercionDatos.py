#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#En este programa insertaremos registros a una BD PostgreSQL

#importamos el paquete para la conexion a la DB
import psycopg2

#inciamos la conexion
conn = psycopg2.connect(host = 'localhost', port = '5432', user = 'postgres', password = ''
                        , dbname = 'testpython')

#iniciamos la sesion
with conn:
    with conn.cursor() as cursor:
        #definimos la sentencia SQL para insertar un registro
        sql = "INSERT INTO Personas (nombre, apellido, email) VALUES (%s, %s, %s)"
        valores = ('Miguel', 'Sanchez', 'msanchez@gmail.com')
        cursor.execute(sql, valores)
        #cursor.connection.commit()
        
        #imprimimos el numero de registros insertados
        registros = cursor.rowcount
        print(f"Se insertaron: {registros} registros")
        
conn.close()
