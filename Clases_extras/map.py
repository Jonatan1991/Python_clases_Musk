numeros = [1, 2, 3, 4, 5]
def duplicar(numeros):
    return numeros * 2

#como se haria normalmente
dobles = []
for n in numeros:
    dobles.append(duplicar(n))
print (dobles)

#con map
dobles = map(duplicar, numeros)
print(list(dobles))