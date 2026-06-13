# Limpia el conjunto de datos y actualiza el archivo
# CSV. Reemplaza todos los valores de las
# columnas que contengan ?, n.a, o NaN.

import pandas as pd
import numpy as np

df = pd.read_csv("Modulo_5/ejercicios/archivos/Modulo5_Automobile_data-221102-123259.csv")

# Reemplazar valores inválidos por NaN real
df = df.replace(["?", "n.a", "NaN"], "desconocido")
df = df.fillna("desconocido")

if df.isna().sum().sum() == 0:
    # Guardar el archivo limpio
    df.to_csv("Modulo_5/ejercicios/archivos/Modulo5_Automobile_data_limpio.csv", index=False)
    print("Archivo limpiado y actualizado correctamente.")
else:
    print("Aún hay valores nulos en el archivo.")