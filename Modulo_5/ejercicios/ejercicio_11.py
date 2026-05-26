# Escribe un programa en Python para convertir
# una cadena de marcas de tiempo unix en una
# fecha legible.
# INPUT Unix timestamp string: 1284105682
# OUTPUT: 2010-09-10 13:31:22

from datetime import datetime

def convertir_unix_a_fecha(unix_timestamp):
    timestamp = int(unix_timestamp)
    fecha_legible = datetime.fromtimestamp(timestamp)
    return fecha_legible

unix_timestamp = "1284105682"
fecha_convertida = convertir_unix_a_fecha(unix_timestamp)
print("Fecha y hora convertida:", fecha_convertida)
