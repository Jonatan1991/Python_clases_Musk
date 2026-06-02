# Combina dos dataframe utilizando la siguiente
# condición. Crea dos dataframe utilizando los
# siguientes dos Dicts, fusiónalos y añade el
# segundo dataframe como una nueva columna al
# primer dataframe.

import pandas as pd

Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925, 71400]}
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182, 160]}

df_Car_Price = pd.DataFrame(Car_Price)
df_car_Horsepower = pd.DataFrame(car_Horsepower)

df_combined = df_Car_Price.merge(df_car_Horsepower, on='Company')
print(df_combined)
