# Lee el beneficio total de cada mes y muéstralo
# utilizando el histograma para ver los rangos de
# beneficio más comunes. 

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Modulo_5/ejercicios/archivos/Modulo5_company_sales_data-221102-123259.csv')

profit = df['total_profit']

plt.hist(profit, bins=12, edgecolor='black')
plt.xlabel('Beneficio total')
plt.ylabel('Frecuencia')
plt.title('Distribución del Beneficio Mensual')
plt.grid(axis='y', alpha=0.4)
plt.show()