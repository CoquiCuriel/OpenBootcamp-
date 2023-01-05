# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 00:19:06 2023

@author: Coqui
"""

class Vehiculo:
    color = "rojo"
    ruedas = 4
    puertas = 4
    
class Coche(Vehiculo):
    velocidad = 150
    cilindrada = 2.8

c = Coche()
print("el color es: ", c.color)
print("Tiene", c.ruedas, "ruedas.")
print("Tiene", c.puertas, "puertas")
print("Velocidad maxima: ", c.velocidad)
print("Velocidad: ", c.velocidad)