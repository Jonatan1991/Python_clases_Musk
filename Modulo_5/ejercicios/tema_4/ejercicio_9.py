# Lee el jabón de baño de todos los meses y
# visualízalo utilizando el Subplot.

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Modulo_5/ejercicios/archivos/Modulo5_company_sales_data-221102-123259.csv')

month = df['month_number']

bathingsoap = df['bathingsoap']
facewash = df['facewash']

plt.subplot(2, 1, 1)
plt.plot(month, bathingsoap, marker='o', label='Jabón de Baño')
plt.xlabel('Mes')
plt.ylabel('Unidades vendidas')
plt.title('Ventas mensuales de Jabón de Baño')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(month, facewash, marker='s', label='Gel de Cara')
plt.xlabel('Mes')
plt.ylabel('Unidades vendidas')
plt.title('Ventas mensuales de Gel de Cara')
plt.legend()

plt.tight_layout()
plt.show()