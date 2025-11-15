# Ejercicio 3

class Jet:
    def __init__(self, name, country, cantidad = 0):
        self.name = name
        self.origin = country
#ejercicio 3
        self.cantidad = cantidad

first_item = Jet("F-16", "USA")
second_item = Jet("SU33", "Russia")
third_item = Jet("AJS37", "Sweden")

#ejercicio 3
fourth_item = Jet("Mirage2000", "France", 35)
fifth_item = Jet("F14", "USA", 87)
#...

sixth_item = Jet("MiG-29", "USSR")
seventh_item = Jet("A-10", "USA")

print(f"Jet Name: {first_item.name}")

