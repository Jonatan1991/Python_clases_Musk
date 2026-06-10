# Calcula los datos de ventas totales del último
# año para cada producto y muéstralos mediante
# un gráfico circular.Nota: En el gráfico circular
# muestra el número de unidades vendidas por año
# para cada producto en porcentaje.


import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Modulo_5/ejercicios/archivos/Modulo5_company_sales_data-221102-123259.csv')

month = df['month_number']
products = df.columns[1:7]

ventas_totales = df[products].sum()
porcentajes = (ventas_totales / ventas_totales.sum()) * 100

plt.figure(figsize=(8, 8))
plt.pie(porcentajes, labels=products, autopct='%1.1f%%')
plt.title('Ventas Totales por Producto')
plt.legend()
plt.show()