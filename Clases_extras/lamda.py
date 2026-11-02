def suma (a, b):
    return a + b

suma_lambda = lambda a, b: a + b

print(suma_lambda(5, 3))


numeros = [1, 2, 3, 4, 5]
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)

pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)