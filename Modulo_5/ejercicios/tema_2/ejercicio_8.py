# Ordena todos los coches por la columna Precio.

import pandas as pd

df = pd.read_csv("Modulo_5/ejercicios/archivos/Modulo5_Automobile_data-221102-123259.csv")

# pd.set_option("display.max_rows", None)

df_sorted = df.sort_values("price", ascending=True)
print(df_sorted)

print()
df_sorted = df.sort_values("price", ascending=False)
print(df_sorted)