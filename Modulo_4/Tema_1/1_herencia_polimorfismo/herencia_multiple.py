class Clase1:
    def metodo_clase1(self):
        print("Soy la clase 1")

class Clase2:
    def metodo_clase2(self):
        print("Soy la clase 2")

class Clase3(Clase1, Clase2):
    pass

c1 = Clase1()
c1.metodo_clase1()

c2 = Clase2()
c2.metodo_clase2()

c3 = Clase3()
c3.metodo_clase1()

