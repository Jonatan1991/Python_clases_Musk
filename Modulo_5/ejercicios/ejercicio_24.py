# Crea una función que calcule la división entre
# dos números. Debe imprimir el mensaje 'Los
# parámetros deben ser número enteros' cuando
# se genera una excepción de tipo y 'El divisor no
# puede ser 0' cuando se genera un
# zerodivisionerror.


def division(x, y):
    try: 
        result = x / y
        return result
    except TypeError:
        print("Los parámetros deben ser números enteros")
    except ZeroDivisionError:
        print("El divisor no puede ser 0")
    

print(division(4, "hola"))
print(division(4, 0))
print(division(4, 2))