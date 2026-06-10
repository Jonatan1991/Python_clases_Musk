# Lee los datos de ventas de los productos crema
# facial y lavado de cara y muéstralos mediante el
# gráfico barras. El gráfico de barras debe mostrar
# el número de unidades vendidas por mes para
# cada producto. Añade de una barra distinta para
# cada producto en el mismo gráfico.

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Modulo_5/ejercicios/archivos/Modulo5_company_sales_data-221102-123259.csv')

month = df['month_number']
facecream = df['facecream']
facewash = df['facewash']

width = 0.35                   # ancho de cada barra


# Barras de facecream
plt.bar(month - width/2, facecream, width, label='Face Cream')

# Barras de facewash
plt.bar(month + width/2, facewash, width, label='Face Wash')
plt.xticks(month)
plt.xlabel('Mes')
plt.ylabel('Unidades vendidas')
plt.title('Ventas mensuales de Face Cream y Face Wash')
plt.legend()
plt.grid(axis='y')

plt.show()
