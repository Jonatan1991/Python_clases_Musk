# Concatena dos dataframes utilizando las
# siguientes condiciones:
# MUSK
# GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925, 71400]}
# japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi'], 'Price': [29995, 23600, 61500, 58
# 900]}

import pandas as pd

GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925, 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi'], 'Price': [29995, 23600, 61500, 58900]}

df_GermanCars = pd.DataFrame(GermanCars)
df_japaneseCars = pd.DataFrame(japaneseCars)

#ignoreindex hace que el indice sea corrido en vez de reiniciarce por cada dataframe qie se concatene
df_concatenado = pd.concat([df_GermanCars, df_japaneseCars], ignore_index=True)
print(df_concatenado)