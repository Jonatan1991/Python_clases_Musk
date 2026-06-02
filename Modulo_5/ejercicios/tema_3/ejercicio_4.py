# Devuelve un array de filas impares y columnas
# pares dado el siguiente array:

import numpy as np
sampleArray = np.array([[ 3,  6,  9, 12], 
                        [15, 18, 21, 24], 
                        [27, 30, 33, 36], 
                        [39, 42, 45, 48], 
                        [51, 54, 57, 60]])

# es decir que tengo que tomar los valores de las columnas pares y las filas impares, donde tanto las filas como las columnas empiezan en 0
# de las filas tengo que tomar las filas 1 y 3 y de las columnas el 0 y 2

resultado = sampleArray[1::2, ::2] #empiezo en la fila 1 y avanzo de 2 en dos (1::2) y las columnas empiezo por la columna 0 y salto de 2 en 2 igual(::2)
print(resultado)