# Divide la matriz en cuatro submatrices de igual
# tamaño. Nota: Crea una matriz de enteros 8x3
# de un rango entre 10 y 34 de tal manera que la
# diferencia entre cada elemento sea 1 y luego
# divide la matriz en cuatro submatrices de igual
# tamaño

import numpy as np

# Crea una matriz de enteros 8x3 de un rango entre 10 y 34
matrix = np.arange(10, 34).reshape(8, 3)

# Divide la matriz en cuatro submatrices de igual tamaño
submatrices = np.split(matrix, 4, axis=0)

print("Submatriz 1:")
print(submatrices[0])
print("\nSubmatriz 2:")
print(submatrices[1])
print("\nSubmatriz 3:")
print(submatrices[2])
print("\nSubmatriz 4:")
print(submatrices[3])