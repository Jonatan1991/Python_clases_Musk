# Crea una función que genere una excepción e
# imprima su tipo, los argumentos de la excepción
# y su mensaje de error.

def suma(x, y):
    try:
        result = x + y
        return result
    except Exception as error:
        print("Type: ", type(error))
        print("Argumentos: ", error.args)
        print("Mensaje de error: ", str(error))


print(suma(1, "Hola"))

