# Definición de la clase base (superclase) que sirve como plantilla
class Animal:
    # Constructor: método especial que se ejecuta al crear un objeto
    def __init__(self, especie, edad):
        # Atributos de instancia: propiedades únicas de cada objeto
        self.especie = especie
        self.edad = edad
    
    # Método polimórfico: definido en la clase base pero será sobrescrito en las subclases
    def hablar(self):
        pass  # Implementación vacía (método abstracto)

    # Método concreto: implementado en la clase base y heredado por las subclases
    def describeme(self):
        print(f"Soy un {self.especie} de {self.edad} años.")

# Subclase 1: hereda atributos y métodos de Animal
class Perro(Animal):
    # Polimorfismo: sobrescritura del método hablar() de la clase padre
    def hablar(self):
        print("Guau!")

# Subclase 2: hereda atributos y métodos de Animal
class Gato(Animal):
    # Polimorfismo: cada subclase tiene su propia implementación de hablar()
    def hablar(self):
        print("Miau!")

# Demostración de polimorfismo: mismo método, diferentes comportamientos según la clase
for animal in (Perro("Rex", 5), Gato("Miau", 3)):  # Instanciación de objetos
    animal.hablar()  # Cada objeto ejecuta su versión del método


# Redefinición de la clase Perro con métodos adicionales
class Perro(Animal):
    def hablar(self):
        print("Guau!")
    
    # Método específico de Perro no presente en la clase base
    def moverse(self):
        print("Camina con 4 patas")

# Subclase 3: nueva clase que hereda de Animal
class Vaca(Animal):
    def hablar(self):
        print("Muu!")
    
    def moverse(self):
        print("Camina con 4 patas")

# Subclase 4: hereda de Animal y añade métodos específicos
class Abeja(Animal):
    def hablar(self):
        print("Bzzzzz!")
    
    def moverse(self):
        print("Vuela")

    # Método exclusivo de la clase Abeja
    def picar(self):
        print("Pica con aguijón")

# Creación de instancias (objetos) de cada subclase
perro = Perro("Rex", 5)
vaca = Vaca("Lola", 4)
abeja = Abeja("Maya", 1)

# Invocación del método heredado describeme() desde la clase Animal
vaca.describeme()
abeja.describeme()

# Invocación del método polimórfico hablar() de cada objeto
perro.hablar()
vaca.hablar()

# Invocación del método específico picar() solo disponible en Abeja
abeja.picar()