#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''El siguiente programa sirve para depurar'''
import logging as log

log.basicConfig(level=log.DEBUG, 
                    format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s', 
                    datefmt= '%I:%M:%S %p',
                    handlers= [log.FileHandler(filename='CapadeDatos.txt', encoding='utf-8', mode= 'w+'),
                               log.StreamHandler()])

if __name__ == '__main__':
    
    log.debug('Mensaje desde Debug')
    log.info('Mensaje desde Info')
    log.warning('Mensaje desde Warning')
    log.critical('Mensaje desde Critical')
    log.error('Mensaje desde Error')
