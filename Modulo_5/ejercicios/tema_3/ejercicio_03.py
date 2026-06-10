# A continuación se muestra el array Numpy
# proporcionado. Devuelve un array de elementos
# tomando la tercera columna de todas las filas.


import numpy as np
sampleArray = np.array([[11,22, 33], 
                        [44, 55, 66], 
                        [77, 88, 99]])

tercera_columna = sampleArray[:, 2]
print(tercera_columna)