"""
Created on Fri Jan 20 15:26:25 2023
@author: Coqui
"""

lista = []

for i in range(5):
    pais = input("Ingresa un pais")
    lista.append(pais)

paises = set(lista)

lista = list(paises)
lista.sort()
print(lista)













