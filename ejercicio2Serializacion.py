"""
Created on Tue Jan 17 16:05:30 2023
@author: Coqui

 SERIALIZACIÓN
"""
import pickle

class Vehiculo:
    marca = ''
    modelo = ''
    color = ''
    precio = 0.0
    
    def __init__(self, marca, modelo, color, precio):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.precio = precio
        
    def getMarca(self):
        return self.marca
    
a1 = Vehiculo('Chevrolet', 'Luv', 'Blanco', 1400000)
print(a1.getMarca(), a1.modelo, 'color', a1.color, 'Precio:', a1.precio)


# ---------cargando datos al fichero---------    
f = open('datos.bin', 'wb')
pickle.dump(a1, f)    
f.close()    
#--------------------------------------------

#---------- Traemos datos desde el fichero-------
f = open('datos.bin', 'rb')
b1 = pickle.load(f)
f.close()

print(b1.getMarca(), b1.modelo)
    
    
    
    
    
    



