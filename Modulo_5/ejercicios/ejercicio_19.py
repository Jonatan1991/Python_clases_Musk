# Implementa un generador de Fibonacci que
# genere n números de la secuencia de Fibonaccі,
# que tiene la forma:
# 0, 1, 1, 2, 3, 5, 8, 13, ...
# Cuyos dos primeros valores son 0 y 1 por
# definición y el resto se calculan sumando los dos
# últimos valores de la sucesión.



# COmo lo piden en el enunciado
def numeros_fibonacci(nums):
    x, y = 0, 1
    for _ in range(nums):
        yield x
        x, y = y, x+y

for num in numeros_fibonacci(10):
    print(num)

# Generador infonito controlado por la llamada a la funcion
def generador_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

numeros = generador_fibonacci()
for _ in range(10):
    print(next(numeros))