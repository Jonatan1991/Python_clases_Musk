
from datetime import date, time

d1 = date (2022, 2, 16)
print(d1)
print(d1.min)
print(d1.max)
#La diferencia más pequeña posible entre objetos de fecha no iguales, timedelta(days=1).
print(d1.resolution)
print(d1.year)
print(d1.month)
print(d1.day)



# Fecha de hoy 
d0 = date.today()
print(d0)

d2 = date (2022, 2, 16)
print(d2)

# Fecha local correspondiente a la marca de tiempo POSIх
d3 = date.fromtimestamp (time.time())
print(d3)   

# Devuelve la fecha correspondiente a sumar un conjunto de días al 1 de enero
# del año 1
d4 = date.fromordinal (730920) # 730920th day after 1. 1. 0001
print(d4)

# Devuelve la fecha codificada en el string yyyy-MM-dd
d5 = date.fromisoformat('2022-02-16')
print(d5)