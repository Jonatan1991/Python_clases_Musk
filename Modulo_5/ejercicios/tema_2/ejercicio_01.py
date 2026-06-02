# Para realizar los ejercicios usar el archivo
# csvAutomobile_data.csv.
# A partir del conjunto de datos dado, imprime las
# cinco primeras y últimas filas.

import pandas as pd

df = pd.read_csv("Modulo_5/ejercicios/archivos/Modulo5_Automobile_data-221102-123259.csv")

print(df.head()) #Head solo mustra los 5 primeros
print()
print(df.tail()) #Tail solo muestra los 5 ultimos (Pero se les puede especificar el número de filas a mostrar)