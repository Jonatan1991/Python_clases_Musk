# Encuentra el coche con el precio más alto de
# precio de cada empresa.

import pandas as pd

df = pd.read_csv("Modulo_5/ejercicios/archivos/Modulo5_Automobile_data-221102-123259.csv")

coche_mas_caro_por_empresa = df.loc[df.groupby("company")["price"].idxmax()]

print(coche_mas_caro_por_empresa)


# df.groupby('native-country')['capital-gain'].agg([len, min, max])
print()
coche_mas_caro = df.groupby("company")["price"].max()
print(coche_mas_caro)

print()
coche_mas_caro = df.groupby("company")["price"].agg("max")
print(coche_mas_caro)