# Limpia el conjunto de datos y actualiza el archivo
# CSV. Reemplaza todos los valores de las
# columnas que contengan ?, n.a, o NaN.

import pandas as pd
import numpy as np

df = pd.read_csv("Modulo_5/ejercicios/archivos/Modulo5_Automobile_data-221102-123259.csv")

df = df.replace(["?", "n.a", "NaN"], "DESCONOCIDO")

df.to_csv("Modulo_5/ejercicios/archivos/Modulo5_Automobile_data_arreglado.csv", index=False)

print("Archivo limpiado y guardado correctamente.")