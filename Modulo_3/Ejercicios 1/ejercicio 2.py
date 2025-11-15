# Ejercicio 2

class Jet:
    def __init__(self, name, country):
        self.name = name
        self.origin = country

first_item = Jet("F-16", "USA")

second_item = Jet("SU33", "Russia")
third_item = Jet("AJS37", "Sweden")
fourth_item = Jet("Mirage2000", "France")
fifth_item = Jet("F14", "USA")
sixth_item = Jet("MiG-29", "USSR")
seventh_item = Jet("A-10", "USA")
# Ejercicio 1
print(f"Jet Name: {first_item.name}")
