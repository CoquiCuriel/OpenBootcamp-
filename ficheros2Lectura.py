"""
Created on Sat Jan  7 17:00:37 2023

@author: Coqui
"""

# FICHEROS2. + BUENAS PRACTICAS

def main():
    usuarios = listarUsuarios()
    for usuario in usuarios:
        print(f'Usuario: {usuario}')
    
def listarUsuarios():
    f = open('passwd.txt', 'r')
    datos = f.readlines()
    f.close()
    
    resultado = []
    for linea in datos:
        if linea[0] == '#' or linea[0] == '\n':
            continue
        
        if linea[0] == '_':
            continue
        
        partes = linea.split(':') #rompemos la cadena en cada :
        resultado.append(partes[0])
        #print(partes[0])

    return resultado

if __name__ == '__main__':
    main()