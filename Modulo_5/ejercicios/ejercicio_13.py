# Escribe un programa en Python para obtener el
# número de la semana.

from datetime import datetime

def numero_semana():
    fecha = datetime.now()
    print("Número de la semana del año :", fecha.strftime("%U"))

numero_semana()