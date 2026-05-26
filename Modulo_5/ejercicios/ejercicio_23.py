# Crea una función que compute la diferencia
# entre dos enteros. En caso de que la diferencia
# sea negativa genera una excepción inventada
# por ti que informe sobre ello. Por ejemplo. la
# excepción podría llamarse
# NegativeDifferenceException.



class NegativeDifferenceException(Exception):
    pass


def diferencia(a, b):
    resultado = a - b
    if resultado < 0:
        raise NegativeDifferenceException(f"La diferencia es negativa: {resultado}")
    return resultado

try:
    print(diferencia(3, 10))   # Lanza excepción
except NegativeDifferenceException as error:
    print("Error:", error)