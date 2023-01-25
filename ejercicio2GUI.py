"""
Created on Tue Jan 24 19:24:12 2023
@author: Coqui
"""

import tkinter

window = tkinter.Tk()
window.geometry('600x400')

titulo = tkinter.Label(window, text='Elija una opcion')
titulo.grid(column=0, row=0)


## Lista de item para seleccionar
lista = ['Hamburguesa', 'Pasta', 'Asado', 'Guiso']
lista_items = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(window, height=5, listvariable=lista_items)
listbox.grid(column=0, row=1, sticky=tkinter.W)




window.mainloop()