# Lee los datos de ventas de jabón de baño de
# todos los meses y muéstralos mediante un
# gráfico de barras.Guarda este gráfico en tu disco
# duro.
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Modulo_5/ejercicios/archivos/Modulo5_company_sales_data-221102-123259.csv')

month = df['month_number']
bathingsoap = df['bathingsoap']

plt.bar(month, bathingsoap, label='Jabón de Baño')
plt.xlabel('Mes')
plt.ylabel('Unidades vendidas')
plt.title('Ventas mensuales de Jabón de Baño')
plt.legend()
plt.savefig('Modulo_5/ejercicios/archivos/ventas_jabon_bano.png')
plt.show()
