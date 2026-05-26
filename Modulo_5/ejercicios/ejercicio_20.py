# Implementa un generador, que dado un entero n,
# imprima todos los números inferiores a n
# multiplicados por dos.

# Solucion 1
def generador(n):
    for x in range(n):
       
       yield x * 2

numeros = generador(5)
for x in numeros:
    print(x)


# Solucion 2 por si el resultado de la multiplicacion es el que debe ser menor que el numero entero n
def generador_2(n):
    for x in range(n):
        num = x * 2
        if num < n:
            yield num
print("\n")
print("Solucion 2")
for i in generador_2(5):
    print(i)