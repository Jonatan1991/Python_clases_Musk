# Crea una matriz de resultados sumando las
# siguientes dos matrices de NumPy. А
# continuación, modifica la matriz de resultados
# calculando el cuadrado de cada elemento.

import numpy as np

arrayone = np.array([[5, 6, 9], [21, 18, 27]])
arrayTwo = np.array([[15 ,33, 24], [4,7, 1]])

result = arrayone + arrayTwo
result = np.square(result)

print(result)