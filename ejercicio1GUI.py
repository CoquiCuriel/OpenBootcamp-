"""
Created on Tue Jan 24 16:00:39 2023
@author: Coqui
"""

import tkinter
from tkinter import ttk



def reiniciar(event):
    print('Reiniciando opciones')
    global opcion
    print(opcion.get())
    opcion = tkinter.StringVar()



window = tkinter.Tk()
window.columnconfigure(0, weight=1)


opcion = tkinter.StringVar()


r1 = ttk.Radiobutton(window, text='Rojo', value='Rojo', variable=opcion)
r2 = ttk.Radiobutton(window, text='Amarillo', value='Amarillo', variable=opcion)
r3 = ttk.Radiobutton(window, text='Verde', value='Verde', variable=opcion)


r1.grid(column=0, row=0, padx=5, pady=5)
r2.grid(column=0, row=1, padx=5, pady=5)
r3.grid(column=0, row=2, padx=5, pady=5)


buttonReiniciar = ttk.Button(window, text='Reiniciar')
buttonReiniciar.grid(column=0, row=4, padx=5, pady=5)
buttonReiniciar.bind('<Button-1>', reiniciar)



window.mainloop()

