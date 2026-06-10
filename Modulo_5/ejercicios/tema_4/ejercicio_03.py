# Lee todos los datos de ventas de productos y
# mostrarlos mediante un gráfico multilínea.
# Muestra el número de unidades vendidas por
# mes para cada producto utilizando gráficos
# multilínea. (es decir, una línea de trazado
# separada para cada producto). 

import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('Modulo_5/ejercicios/archivos/Modulo5_company_sales_data-221102-123259.csv')

months = df['month_number']
product = df.columns[1:7]  # no tomo las filas pero tomo las columnas desde el indice 1 al 7

# for col in product:
#     plt.plot(months, df[col], label=col, marker='o')

# plt.xlabel('Número de mes')
# plt.ylabel('Unidades vendidas')
# plt.legend()
# plt.show()


df.plot(x='month_number', y=product, marker='o')

plt.xlabel('Número de mes')
plt.ylabel('Unidades vendidas')
plt.title('Ventas mensuales por producto')
plt.grid(True)
plt.show()