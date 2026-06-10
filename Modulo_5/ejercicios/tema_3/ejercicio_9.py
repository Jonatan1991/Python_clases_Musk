# Elimina la segunda columna de una matriz dada е
# inserta la siguiente columna nueva en su lugar.

import numpy as np
sampleArray = np.array([[34,43,73], 
                        [82,22,12], 
                        [53,94,66]])

newColumn = np.array([[10,10,10]])

sampleArray = np.delete(sampleArray, 1, axis=1)
sampleArray = np.insert(sampleArray, 1, newColumn, axis=1)  

print(sampleArray)