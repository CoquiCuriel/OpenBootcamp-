# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 00:27:12 2023

@author: Coqui
"""

class Alumno:
    nombre = ""
    nota = 0
    
    def cargarNombre(self, nombre):
        self.nombre = nombre
        print("nombre cargado:", nombre)
        
    def cargarNota(self, nota):
        self.nota = nota
        print("nota cargada: ", nota)
        
    def mostrar(self):
        if self.nota > 7:
            print("la nota es: ", self.nota, ": APROBADO")
        else:
            print("la nota es: ", self.nota, ": DESAPROBADO")
        
   
a = Alumno()
a.cargarNombre("Pepe")   
a.cargarNota(8)
a.mostrar()

b = Alumno()
b.cargarNombre("Juan")  
b.cargarNota(4)
b.mostrar()
   
    
   