# Imprime el máximo del eje 0 y el mínimo del eje 1
# de la siguiente matriz bidimensional:

import numpy as np
sampleArray = np.array([[34,43,73],
                        [82,22,12], 
                        [53,94,66]])

max_eje0 = np.max(sampleArray, axis=0)
min_eje1 = np.min(sampleArray, axis=1)

print("Máximo del eje 0:")
print(max_eje0)

print("Mínimo del eje 1:")
print(min_eje1)

