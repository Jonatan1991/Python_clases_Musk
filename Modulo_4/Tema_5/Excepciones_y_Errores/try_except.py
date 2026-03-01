import sys

try:
    f = open('numeros.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as (errno, strerror):
    print("Error E/S ({0}): {1}".format(errno, strerror))
except ValueError:
    print("No pude convertir el dato a un entero.")
except:
    print("Error inesperado:", sys.exc_info() [0])

try:
    d = 2 + "Hola"
except Exception as ex:
    print("Ha habido una excepción", type(ex))

try:
    x = 10/0
except:
    print("Entra en except, ha ocurrido una excepción")
else:
    print("Entra en else, no ha ocurrido ninguna excepción")

try:
# La división puede realizarse sin problema
    x = 10/2
except:
    print("Entra en except, ha ocurrido una excepción")
else:
    print("Entra en else, no ha ocurrido ninguna excepción")