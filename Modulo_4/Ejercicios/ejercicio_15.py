# Escribe un programa en Python para contar el
# número de lunes del primer día del mes desde
# 2015 hasta 2016.


from datetime import datetime, timedelta

def cantidad_lunes():

    count_lunes = 0
    fecha = datetime(2015, 1, 1)

    while fecha.year < 2016:
        if fecha.weekday() == 0:
            count_lunes += 1
        fecha += timedelta(days=1)

    return count_lunes


print("La cantidad de lunes que tiene el año 2015 es: ", cantidad_lunes(), "lunes")