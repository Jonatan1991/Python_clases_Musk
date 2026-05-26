# Escribe un programa en Python para crear 12
# fechas fijas a partir de una fecha especificada en
# un periodo determinado. La diferencia entre dos
# fechas será de 20.

from datetime import datetime, timedelta

def fechas():

    fecha_especifica = datetime(2000, 2, 4)
    count = 1

    while count <= 12:
        print(fecha_especifica.strftime("%A %d %B %Y"))
        fecha_especifica += timedelta(days = 20)
        count += 1


print(fechas())

# Respuesta con return y una lista, porque al final me devuelve un none con la respuesta anterior
def fechas_2():

    fecha_especificada = datetime(2003, 3, 28)
    count = 0
    lista_fechas = []

    while count <= 11:
        lista_fechas.append(fecha_especificada.strftime("%A %d %B %Y"))
        fecha_especificada += timedelta(days=20)
        count += 1

    return lista_fechas

for fecha in fechas_2():
    print(fecha)
