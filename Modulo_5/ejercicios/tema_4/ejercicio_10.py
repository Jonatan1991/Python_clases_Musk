# Lee todos los datos de las ventas de productos y
# muéstrelos mediante el diagrama de pila.

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Modulo_5/ejercicios/archivos/Modulo5_company_sales_data-221102-123259.csv')

month = df['month_number']
products = df.columns[1:7]

plt.stackplot(month, df[products].T, labels=products)
plt.xlabel('Mes')
plt.ylabel('Unidades vendidas')
plt.title('Ventas mensuales por producto')
plt.legend()
plt.show()