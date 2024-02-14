'''
Este archivo contiene el logger para el manejo de mensajes de depuracion del proyecto
'''

import logging as log

log.basicConfig(level = log.ERROR,
                format = '%(asctime)s:%(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt = '%I:%M:%S %p',
                handlers= [log.FileHandler(filename='Usuario.txt', encoding='utf-8', mode='w+'),
                           log.StreamHandler()])

if __name__ == '__main__':
    log.info('Prueba del logger')
