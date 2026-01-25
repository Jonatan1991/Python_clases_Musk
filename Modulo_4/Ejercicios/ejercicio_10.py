# Escribe un programa en Python para restar cinco
# días a la fecha actual.


from datetime import datetime, timedelta

fecha_actual = datetime.now()
dias_a_restar = 5
nueva_fecha = fecha_actual - timedelta(days = dias_a_restar)

print("5 dias atras de la fecha actual: ")
print(nueva_fecha)