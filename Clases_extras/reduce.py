from functools import reduce
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

suma = 0
for numero in numeros:
    suma += numero*3
print(suma)

def agregadopor3(acumulador, numero):
    return acumulador + numero * 3


suma = reduce(agregadopor3, numeros)
print(suma)