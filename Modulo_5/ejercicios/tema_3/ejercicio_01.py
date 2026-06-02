# Crea un array de enteros 4X2 e imprime sus
# atributos. Nota: El elemento debe ser de tipo
# unsignedint16. Imprime los siguientes atributos:
# La shape del array.
# Las dimensiones del array.
# El tamaño de cada elemento del array en bytes.

import numpy as np

# array = np.empty((4, 2), dtype=np.uint16)

array = np.array([[1, 2], [3, 4], [5, 6], [7, 8]], dtype=np.uint16)
print("Shape del array:", array.shape)
print("Dimensiones del array:", array.ndim)
print("Tamaño de cada elemento en bytes:", array.itemsize)


array_2 = np.random.randint(0, 20, size=(4, 2), dtype=np.uint16)

print(array_2)
print("Shape del array:", array_2.shape)
print("Dimensiones del array:", array_2.ndim)
print("Tamaño de cada elemento en bytes:", array_2.itemsize)