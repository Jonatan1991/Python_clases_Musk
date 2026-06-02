# Encuentra el kilometraje medio de cada empresa
# fabricante de automóviles.

import pandas as pd

df = pd.read_csv("Modulo_5/ejercicios/archivos/Modulo5_Automobile_data-221102-123259.csv")

#mean calcula la media
kilometraje_medio_empresa = df.groupby("company")["average-mileage"].mean()
print(kilometraje_medio_empresa)