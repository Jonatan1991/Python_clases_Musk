# Escribe un programa en Python para seleccionar
# todos los domingos de un año determinado.


from datetime import datetime, timedelta

def domingos_anno(anno):

    fecha = datetime(anno, 1, 1)
    #print(anno)
    #print(fecha.strftime("%Y"))
    #print(fecha.strftime("%A"))

    while fecha.strftime("%Y") == str(anno):
        fecha = fecha + timedelta(days = 1)
        if fecha.strftime("%A") == "Sunday":
            print(fecha.strftime("%A %d %B %Y"))


# domingos_anno(2025)


# Otra forma, pero con menos iteraciones y modificaciones:

def domingos_x_anno(anno):
    fecha = datetime(anno, 1, 1)

    while fecha.weekday() != 6:
        fecha += timedelta(days=1)
        

    while fecha.year == anno:
        print(fecha.strftime("%A %d %B %Y"))
        fecha += timedelta(days=7)
            

domingos_x_anno(2026)
        



