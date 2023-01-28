"""
Created on Fri Jan 27 20:06:16 2023
@author: Coqui
"""

import sqlite3


def buscar(nombre):
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()

    rows = cursor.execute(f"SELECT * FROM Alumnos WHERE nombre='{nombre}'")  
    return rows

    cursor.close()
    conn.close()
 

def main():
    nombre = input("Ingrese un nombre para buscar: ")
    
    resultado = buscar(nombre)
    
    for row in resultado:
        print(row)


if __name__ == '__main__':
    main()
