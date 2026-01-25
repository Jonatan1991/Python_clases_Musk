# Escribe un script en Python para mostrar los
# distintos formatos de fecha y hora.
# a) Fecha y hora actuales
# b) Año actual
# c) Mes del año
# d) Número de la semana del año
# e) Día de la semana
# f) Día del año
# g) Día del mes
# h) Día de la semana

from datetime import datetime

def fecha_hora_actual(fecha):
    print("Fecha y hora actuales: ", fecha)

def año_actual(fecha):
    print("Año actual: ", fecha.strftime("%Y"))

def mes_actual(fecha):
    print("Mes del año: ", fecha.strftime("%m"))

def numero_semana(fecha):
    print("Número de la semana del año :", fecha.strftime("%U"))

def dia_semana(fecha):
    print("Día de la semana: ", fecha.strftime("%A"))

def dia_año(fecha):
    print("Día del año: ", fecha.strftime("%j"))

def dia_mes(fecha):
    print("Día del mes: ", fecha.strftime("%d"))

def dia_semana_numero(fecha):
    print("Día de la semana:", fecha.strftime("%w"))

print("Formatos de fecha y hora:")

fecha = datetime.now()

fecha_hora_actual(fecha)

año_actual(fecha)

mes_actual(fecha)

numero_semana(fecha)

dia_semana(fecha)

dia_año(fecha)   

dia_mes(fecha)

dia_semana_numero(fecha)
