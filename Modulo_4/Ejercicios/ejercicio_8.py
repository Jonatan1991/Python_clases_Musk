# Escribe un programa en Python para convertir
# una cadena a datetime.
# INPUT: Jan 1 2014 2:43PM
# OUTPUT: 2014-07-01 14:43:00

from datetime import datetime

def convertir_cadena_a_datetime(cadena):
    formato = "%b %d %Y %I:%M%p"
    fecha_datetime = datetime.strptime(cadena, formato)
    return fecha_datetime

cadena_fecha = "Jan 1 2014 2:43PM"
fecha_convertida = convertir_cadena_a_datetime(cadena_fecha)
print("Fecha y hora convertida:", fecha_convertida)