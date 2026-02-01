# Añade a la función anterior, un mensaje que se
# imprima al final de la ejecución de la función
# independientemente de si se ha generado
# excepción o no.



def division(x, y):
    try: 
        result = x / y
        return result
    except TypeError:
        print("Los parámetros deben ser números enteros")
    except ZeroDivisionError:
        print("El divisor no puede ser 0")
    finally:
        print("Este es el último ejercicio para finalizar el modulo 4")

print(division(4, "hola"))
print(division(4, 0))
print(division(4, 2))