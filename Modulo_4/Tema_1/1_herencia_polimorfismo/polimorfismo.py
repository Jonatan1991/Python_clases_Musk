# El polimorfismo permite que objetos de diferentes clases respondan al mismo método u operador
# de maneras diferentes. Aquí hay dos ejemplos de polimorfismo:

# 1. Polimorfismo de operadores - Sobrecarga del operador +
class Coord:
    def __init__(self, x =0 , y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '{}, {}'.format(self.x, self.y)
    
    # La sobrecarga del operador + permite usar el operador con objetos Coord
    # redefiniendo cómo se comporta la suma para esta clase específica
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Coord(x, y)
    
c1 = Coord(2, 3)
c2 = Coord(5, 7)
print(c1 + c2)  # El operador + funciona de forma diferente con Coord que con números

# 2. Polimorfismo de métodos - Mismo nombre, diferente comportamiento
class Foo:
    def test(self):  # Método test en clase Foo
        print("Método de la clase Foo")

class Bar:
    def test(self):  # Mismo método test pero en clase Bar, con diferente comportamiento
        print("Método de la clase Bar")

foo = Foo()
bar = Bar()

# Aunque foo y bar son de diferentes clases, ambos responden al método test()
# pero cada uno lo implementa de manera diferente
print(type(foo))
print(type(bar))
print(isinstance(bar, type(foo)))

# Llamando al mismo método en diferentes objetos
Foo().test()  # Ejecuta la versión de Foo
Bar().test()  # Ejecuta la versión de Bar