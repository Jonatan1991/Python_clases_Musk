# Escribe un programa en Python para sumar 5
# segundos con la hora actual


from datetime import datetime, timedelta

hora_actual = datetime.now()
segundos_a_sumar = 5
nueva_hora = hora_actual + timedelta(seconds = segundos_a_sumar)

print("5 segundos adelante de la hora actual: ")
print(nueva_hora.time())