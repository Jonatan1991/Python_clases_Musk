lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def par (numero):
    if numero % 2 == 0:
        return True
    else:
        return False

#como se haria normalmente
pares = []
for n in lista:
    if par(n):
        pares.append(n)
print(pares)

#con filter
pares = filter(par, lista)
print(list(pares))