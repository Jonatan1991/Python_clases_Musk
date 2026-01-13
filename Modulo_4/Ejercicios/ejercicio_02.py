# Representa el siguiente diagrama con sus clases,
# atributos y métodos correspondientes.
# Cada método display debe imprimir el nombre de
# la clase, atributos y valores de la instancia en ese
# momento. Ejemplo: In
# displaymethodofParent1x=10

class Parent1():
    def __init__(self, x):
        self.x = x
    
    def display(self):
        print(f"IndisplaymethodofParent1: x = {self.x}")


class Parent2():
    def __init__(self, y):
        self.y = y

    def display(self):
        print(f"IndisplaymethodofParent2: y = {self.x}")

class Child(Parent1, Parent2):
    def __init__(self, x, y, z):
        Parent1.__init__(self, x)
        Parent2.__init__(self, y)
        self.z = z

    def display(self):
        print(f"IndisplaymethodofChild:  x = {self.x}, y = {self.y}, z = {self.z}")

obj = Child(10, 20, 30)
obj.display()

obj1 = Parent1(12)
obj1.display()

obj2 = Parent1(13)
obj2.display()