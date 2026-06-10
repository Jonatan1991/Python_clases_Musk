# Obtenga el beneficio total de todos los meses y
# muestre un gráfico de líneas con las siguientes
# propiedades de estilo:
# •Estilo de línea punteada y el color de la línea
# debe ser rojo
# •Mostrar la leyenda en la parte inferior derecha.
# •Nombre de la etiqueta X = Número de mes
# •Nombre de la etiqueta Y = Número de
# •unidades vendidas
# •Añadir un marcador de círculo.
# •El ancho de la línea debe ser 3

import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('Modulo_5/ejercicios/archivos/Modulo5_company_sales_data-221102-123259.csv')

month = df['month_number']
units_sold = df['total_units']

plt.plot(month, units_sold, linestyle='--', color='red', linewidth=3, marker='o')
plt.xlabel('Número de mes')
plt.ylabel('Unidades vendidas')
plt.legend(['Unidades vendidas'], loc='lower right')
plt.show()