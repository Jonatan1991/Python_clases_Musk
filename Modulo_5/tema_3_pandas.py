import pandas as pd

dictionary = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]}

#create a series
series = pd.Series(dictionary)

print(series)