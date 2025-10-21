#CREACION DE LA CLASE COCHE
class Coche:
    #constructor de la clase
    def __init__(self, color:str, marca:str, num_puertas:int, anno = 2024):
        self.color = color
        self.marca = marca
        self.num_puertas = num_puertas
        #atributo por defecto que no se puede cambiara nivel de usuario
        self.num_ruedas = 4
        #atributo por defecto pero se puede cambiar por el usuario porque lo pide por atributo
        self.anno = anno

#instancia de la clase coche (coche1 y coche2)
coche1 = Coche("rojo", "Audi", 2, 2025)
coche2 = Coche("verde", "Lada", 4)

print(coche1.num_puertas)


#Atributos de Clase
class Persona:
    raza = "humano"

    def __init__(self):
        pass

Persona.raza


class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def hablar(self, mensaje):
        return mensaje
    def saludar(self):
        return 'hola'
    def informacion(self):
        print(f"tu nombre es {self.nombre} y tu apellido es {self.apellido}")
    
persona1 = Persona('Jona', 'Aguila')
print(persona1.hablar("hola que tal"))
print(persona1.hablar("como te llamas"))

print(persona1.saludar())

persona1.informacion()


#METODO DE INSTANCIA
print(".................................................................")
class Persona:
    def __init__(self, nombre, apellido, nacimeinto):
        self.nombre = nombre
        self.apellido = apellido
        self.nacimiento = nacimeinto

    def hablar(self, mensaje):
        return mensaje
    
    def saludar(self):
        return "hola"
    
    def calculo_edad(self):
        edad = 2025 - self.nacimiento
        return edad
    
    def informacion(self):
        print(f"tu nombre es {self.nombre} y tu apellido es {self.apellido}, y tu edad es {self.calculo_edad()}")

    def categoria_edad(self):
        categoria = ""
        if self.calculo_edad() < 18:
            categoria = "nino"
        elif self.calculo_edad < 80:
            categoria = "adulto"
        else:
            categoria = "tercera edad"

        return categoria
    
person1 = Persona("felix", "martin", 1991)
person2 = Persona("jona", "Aguial", 2000)

print(person1.hablar("hola como estas"))
palabras = "esto es lo que esta hablando"

print(person2.hablar(palabras))

print(person1.saludar())

person1.informacion()
person2.informacion()