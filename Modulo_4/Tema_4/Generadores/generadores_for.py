def contador_hasta(n):
    for i in range(1, n + 1):
        yield i

# Usamos el generador
for numero in contador_hasta(5):
    print(numero)
