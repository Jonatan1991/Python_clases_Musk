# Para resolver estos ejercicios debes usar el
# fichero csvcompany_sales_data.csv.

# Lee el beneficio total de todos los meses y
# muéstralo mediante un gráfico de líneas. Se
# proporcionan los datos del beneficio total de
# cada mes. El gráfico de líneas generado debe
# incluir las siguientes propiedades:
# Nombre de la etiqueta X = Número de mes
# Nombre de la etiqueta Y = Beneficio total

import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('Modulo_5/ejercicios/archivos/Modulo5_company_sales_data-221102-123259.csv')

# Obtener los datos de los meses y el beneficio total
months = df['month_number']
total_profit = df['total_profit']

# Crear el gráfico de líneas
plt.plot(months, total_profit)
plt.xlabel('Número de mes')
plt.ylabel('Beneficio total')
plt.grid(True)
plt.title('Beneficio Total por Mes')
plt.show()