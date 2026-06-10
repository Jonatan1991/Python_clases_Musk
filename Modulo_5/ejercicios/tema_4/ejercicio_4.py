# Lee los datos de las ventas de pasta de dientes
# de cada mes y muéstralos mediante un gráfico
# de dispersión (scatter). Además, añade una
# cuadrícula en el gráfico. El estilo de la cuadrícula
# debe ser "-".

import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('Modulo_5/ejercicios/archivos/Modulo5_company_sales_data-221102-123259.csv')

month = df['month_number']
pasta_sales = df['toothpaste']

plt.scatter(month, pasta_sales)
plt.grid(True, linestyle='--')
plt.xlabel('Mes')
plt.ylabel('Número de unidades vendidas')
plt.title('Ventas pasta de dientes')
plt.show()