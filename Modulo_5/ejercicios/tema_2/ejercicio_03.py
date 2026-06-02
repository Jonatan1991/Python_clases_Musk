# Encuentra el nombre de la empresa del coche
# más caro. Imprime el nombre de la empresa del
# coche más caro y su precio.


import pandas as pd


df = pd.read_csv("Modulo_5/ejercicios/archivos/Modulo5_Automobile_data_arreglado.csv")

max_price = df["price"].max()
print(max_price)
car = df[df["price"] == max_price]
print(car)
print()

print(f"La empresa del coche más caro es: {car['company'].iloc[0]} y su precio es: {max_price}")


print()
print()
print()
caro = df.loc[df["price"].idxmax()]

print("Empresa:", caro["company"])
print("Precio:", caro["price"])