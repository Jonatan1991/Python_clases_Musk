# Imprime todos los datos de los coches Toyota.

import pandas as pd

df = pd.read_csv("Modulo_5/ejercicios/archivos/Modulo5_Automobile_data_arreglado.csv")
coche_toyota = df[df["company"] == "toyota"]
print(coche_toyota)