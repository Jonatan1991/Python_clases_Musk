# Crea una matriz de enteros 5X2 de un rango
# entre 100 y 200 tal que la diferencia entre cada
# elemento sea 10

import numpy as np

matrix = np.arange(100, 200, 10).reshape(5, 2)

print(matrix)