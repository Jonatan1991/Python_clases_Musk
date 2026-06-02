# Cuenta el total de coches por empresa.

import pandas as pd

df = pd.read_csv("Modulo_5/ejercicios/archivos/Modulo5_Automobile_data-221102-123259.csv")

coches_por_empresa = df.groupby("company").size()
print(coches_por_empresa)

print()
coches_empresa = df['company'].value_counts()
print(coches_empresa)