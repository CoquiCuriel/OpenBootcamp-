# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 23:46:57 2022

@author: Coqui
"""

# AÑO BISIESTO

def bisiesto(*args):
    local = []
    for i in args:
        if i % 4 == 0:
            aux = str(i) + " Es bisiesto"
            local.append(aux)          
        else:
           aux = str(i) + " No es bisiesto"
           local.append(aux)  
           
    return local

respuestas = bisiesto(1988, 1992, 1996, 2022)
print(respuestas)