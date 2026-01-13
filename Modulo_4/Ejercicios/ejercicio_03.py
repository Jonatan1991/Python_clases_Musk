# Crea una clase Car que herede de Vehicle y que
# sobreescriba los métodos max_speed() y
# change_gear(). Instancia dos objetos de cada
# clase y compruebaque la salida de cada método
# es distinta

class Vehicle:
    def __init__ (self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print('Details:', self.name, self.color, self.price)

    def max_speed(self):
        print('Vehicle max speed is 150')

    def change_gear(self):
        print('Vehicle change 6 gear')

# Nueva clase que hereda de la clase Vehicle
class Car(Vehicle):
    # Sobreescritura del metodo max_speed
    def max_speed(self):
        print("Vehicle max speed is 240 Km/h")

     # Sobreescritura del metodo change_gear
    def change_gear(self):
        print('Vehicle change 12 gear')

# Instancia 1 de la clase Vehicle
vehiculo1 = Vehicle('Toyota', 'rojo', 14000)
# Mostrar los resultados
vehiculo1.show()
vehiculo1.max_speed()
vehiculo1.change_gear()

print('\n')

# Instancia 2 de la clase Vehicle
vehiculo2 = Vehicle('Ford', 'blanco', 17000)
# Mostrar los resultados
vehiculo2.show()
vehiculo2.max_speed()
vehiculo2.change_gear()

print('\n')

# Instancia 1 de la clase Car
car1 = Car('Volvo', 'negro', 50000)
# Mostrar los resultados
car1.show()
car1.max_speed()
car1.change_gear()

print('\n')

# Instancia 2 de la clase Car
car2 = Car('Mercedez', 'Azul', 42000)
# Mostrar los resultados
car2.show()
car2.max_speed()
car2.change_gear()