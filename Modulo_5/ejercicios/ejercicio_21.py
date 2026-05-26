#Implementa un generador, que dado un entero n,
#genere n número senares.


import random

def numeros_senares(n):
    for _ in range(n):
        numero = random.randint(1, 99)
        if numero % 2 != 0:
            yield numero
        else:
            numero = numero - 1
            yield numero

for impar in numeros_senares(10):
    print(impar)