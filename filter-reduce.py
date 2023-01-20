"""
Created on Fri Jan 20 16:20:44 2023
@author: Coqui
"""
from functools import reduce

def verifica(x):
    if x % 2 == 0:
        return False
    else:
        return True

def suma(a, b):
    return a + b    


numeros = [2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 14]

impares = filter(verifica, numeros)
impares = list(impares)
print(f'Los numeros impares son: {impares}')


total = reduce(suma, impares)
print(f'La suma de ellos es: {total}')












