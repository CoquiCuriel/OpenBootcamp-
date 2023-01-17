# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 11:43:51 2023

@author: Coqui
"""

# Creamos el fichero
f = open('ficheroTarea.txt', 'w')
f.close()


datos = ['una cadena', '23', 'otra mas']

# Agregamos texto al fichero
f = open('ficheroTarea.txt', 'a')
f.writelines(datos)
f.close()
