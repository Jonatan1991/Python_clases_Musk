class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    
    def hablar(self):
        pass

    def describeme(self):
        print(f"Soy un {self.especie} de {self.edad} años.")

class Perro(Animal):
    def hablar(self):
        print("Guau!")

class Gato(Animal):
    def hablar(self):
        print("Miau!")

for animal in (Perro("Rex", 5), Gato("Miau", 3)):
    animal.hablar()


class Perro(Animal):
    def hablar(self):
        print("Guau!")
    
    def moverse(self):
        print("Camina con 4 patas")

class Vaca(Animal):
    def hablar(self):
        print("Muu!")
    
    def moverse(self):
        print("Camina con 4 patas")

class Abeja(Animal):
    def hablar(self):
        print("Bzzzzz!")
    
    def moverse(self):
        print("Vuela")

    def picar(self):
        print("Pica con aguijón")

perro = Perro("Rex", 5)
vaca = Vaca("Lola", 4)
abeja = Abeja("Maya", 1)

vaca.describeme()
abeja.describeme()

perro.hablar()
vaca.hablar()

abeja.picar()