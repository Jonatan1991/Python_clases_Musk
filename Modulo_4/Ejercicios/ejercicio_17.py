# Implementa una función generadora que dadas
# dos listas del mismo tamaño, devuelva la
# multiplicación entre los elementos de cada una,
# el primer elemento de la lista 1 por el primero de
# la lista 2, el segundo con el segundo y así
# sucesivamente. Sigue la siguiente estructura:

# def prod(l1, 12):

# except StopIteration:
# pass
# return solution

# Añadiendo el bloque except capturamos la
# excepción de Stop Iteration que se produce al
# acabar de leer todos los elementos de un
# generador.


def prod(l1, l2):
    it1 = iter(l1)
    it2 = iter(l2)

    try:
        while True:
           solution =  yield next(it1) * next(it2)
    except StopIteration:
        pass
    return solution

list_1 = [1, 2, 3, 4, 5, 6, 7]
list_2 = [2, 4, 6, 7, 9, 3, 1]

resultado = prod(list_1, list_2)

for i in resultado:
    print(i)