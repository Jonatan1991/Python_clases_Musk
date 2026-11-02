from functools import reduce
def suma (a, b):
    return a + b

suma_lambda = lambda a, b: a + b

print(suma_lambda(5, 3))


numeros = [1, 2, 3, 4, 5]
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)

pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

alumnos = dict(Luis=5.5, Ana=9.0, Carlos=7.5)
nuevasnotas = dict(map(lambda item: (item[0], item[1] + 0.5), alumnos.items()))
print(nuevasnotas)

aprobados = dict(filter(lambda item: item[1] >= 8.0, nuevasnotas.items()))
print(aprobados)

medianotas = reduce(lambda a, b: a + b, nuevasnotas.values()) / len(nuevasnotas)
print(medianotas)