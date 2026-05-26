# Implementa un generador, que dado un entero n,
# genere n números aleatorios. Puedes usar el
# método random de la librería random para
# generar números aleatorios.

import random

def numeros_random(n):
    for _ in range(n):
       
        # yield random.random() # asi me devuelve numeros decimales random
       
        yield random.randint(1, 100) #asi me devuelve nuemros random enteros

numeros = numeros_random(7)
for num in numeros:
    print(num)