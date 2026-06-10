# Ordena el siguiente array de NumPy:
# Caso 1: Ordenar el array por la segunda fila
# Caso 2: Ordenar el array por la segunda columna


import numpy as np

sampleArray = np.array([[34,43,73], 
                        [82,22,12], 
                        [53,94,66]])

# argsort devuelve los índices ordenados
# Ordenar por la segunda fila
orden = np.argsort(sampleArray[1])
# ya en orden tenemos las filas ordenadas
resultado1 = sampleArray[:, orden]

print("Array ordenado por la segunda fila:")
print(resultado1)


# Ordenar por la segunda columna 
orden = np.argsort(sampleArray[:, 1])
resultado2 = sampleArray[orden, :]

print("Array ordenado por la segunda columna:")
print(resultado2)
