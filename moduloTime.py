# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 23:56:16 2023

@author: Coqui
"""

from datetime import datetime

actual = datetime.now()
actual = actual.strftime("%H:%M")
actual = datetime.strptime(actual, "%H:%M")
print("Hora actual:", actual.strftime("%H:%M"))


salida = datetime(2023, 1, 6, 19,0,0)
salida = salida.strftime("%H:%M")
salida = datetime.strptime(salida, "%H:%M")
print("Hora de salida:", salida.strftime("%H:%M"))


descansando = datetime(2023, 1, 6, 8,0,0)
descansando = descansando.strftime("%H:%M")
descansando = datetime.strptime(descansando, "%H:%M")


if actual > descansando and actual < salida:
    print("Falta para salir:", salida-actual, "horas")
else:
    print("Tiempo de descanso")







