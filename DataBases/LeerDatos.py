#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#En este proyecto nos conectaremos a una base de datos PostgresSQL con with

import psycopg2 #importamos el paquete para DB

#iniciamos la autenticacion
conn = psycopg2.connect(host='localhost', user='postgres', password='', dbname='testpython', port='5432')

#iniciamos la conexion y uso
with conn:
    with conn.cursor() as cursor:
        sql = "SELECT nombre, apellido, email FROM Personas WHERE id_personas IN(%s, %s, %s)"
        
        #obtenemos los valores
        id = input("Ingrese los id requeridos separados por comas y espacios: ")
        
        #usamos el metodo split para separarlos y convertirlo a una cadena
        valores = id.split(', ') #usamos la comay el espacio como separadores
        cursor.execute(sql, valores)
        registros = cursor.fetchone()
        print(registros)
        
conn.close()
