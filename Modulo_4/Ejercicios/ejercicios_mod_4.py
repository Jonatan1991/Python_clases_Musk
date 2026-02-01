# Ejercicio 1

# Crea una clase Staff con los atributos role, depty
# salary. crea una clase profesor que herede de la
# clase anterior y que además tenga como
# atributos nombre y edad. haz que sea posible
# instanciar un profesor dándole valor a todos los
# atributos.

# Clase base Staff
class Staff:
    # constructor
    def __init__(self, role, depty, salary):
        #atributos
        self.role = role
        self.depty = depty
        self.salary = salary

# Clase Profesor, hereda de la clase padre Staff
class Profesor(Staff):
    def __init__(self, role, depty, salary, nombre, edad):
        super().__init__(role, depty, salary)
        self.nombre = nombre
        self.edad = edad

#Instancia de Profesor
profesor = Profesor(
    role= "catedratico",
    depty = "ciencia",
    salary = 1750,
    nombre = "Juan",
    edad = 45,
)

print(f"El profesor {profesor.role} {profesor.nombre} es del departamento {profesor.depty} con un salario de {profesor.salary} euros y tiene una edad de {profesor.edad} años")

#################################################################################
#Ejercicio 2

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

#################################################################################
#Ejercicio 3

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

#################################################################################
#Ejercicio 4

"""
Dadas las siguientes clases con el output de sus
respectivos métodos, crea una interfaz formal
que las implemente.

svm = SVM()
svm.preprocess_data(data=None, y=None)
svm.fit()
svm.predict()
dt = DecisionTree()
dt.preprocess_data(data=None, y=None)
dt.fit(O)
dt.predict()

output:
Preprocessing data at SVM
Training at SVM
Evaluating at SVM
Preprocessing data at DecisionTree
Training at DecisionTree
Evaluating at DecisionTree

Preprocessing data at SVM
Training at SVM
Evaluating at SVM
Preprocessing data at DecisionTree
Training at DecisionTree
Evaluating at DecisionTree

"""

from abc import abstractmethod
from abc import ABCMeta

class Interfaz(metaclass=ABCMeta):

    @abstractmethod
    def preprocess_data(self, data, y):
        pass

    @abstractmethod
    def fit(self):
        pass

    @abstractmethod
    def predict(self):
        pass

class SVM(Interfaz):

    def preprocess_data(self, data, y):
        self.data = data
        self.y = y

        print('Preprocessing data at SVM')

    def fit(self):
        print('Training at SVM')

    def predict(self):
        print('Evaluating at SVM')

class DecisionTree(Interfaz):

    def preprocess_data(self, data, y):
        self.data = data
        self.y = y
        print('Preprocessing data at DecisionTree')

    def fit(self):
        print('Training at DecisionTree')

    def predict(self):
        print('Evaluating at DecisionTree')

svm = SVM()
svm.preprocess_data(data=None, y=None)
svm.fit()
svm.predict()

dt = DecisionTree()
dt.preprocess_data(data=None, y=None)
dt.fit()
dt.predict()

#################################################################################
#Ejercicio 5

# Repite el ejercicio anterior esta vez creando una
# interfaz informal.


class Interfaz:
    def preprocess_data(self):
        pass
    def fit(self):
        pass
    def predict(self):
        pass

class SVM(Interfaz):

    def preprocess_data(self, data, y):
        self.data = data
        self.y = y

        print('Preprocessing data at SVM')

    def fit(self):
        print('Training at SVM')

    def predict(self):
        print('Evaluating at SVM')

class DecisionTree(Interfaz):

    def preprocess_data(self, data, y):
        self.data = data
        self.y = y
        print('Preprocessing data at DecisionTree')

    def fit(self):
        print('Training at DecisionTree')

    def predict(self):
        print('Evaluating at DecisionTree')

svm = SVM()
svm.preprocess_data(data=None, y=None)
svm.fit()
svm.predict()

dt = DecisionTree()
dt.preprocess_data(data=None, y=None)
dt.fit()
dt.predict()

#################################################################################
#Ejercicio 6

# Crea una clase virtual llamada Algoritmo con los
# atributos nombre, tarea y aprendizaje que sea
# superclase de la clase BaseClassifier del
# problema anterior. Comprueba con el método
# issubclass que Algoritmo es padre de
# BaseClassifier.

from abc import ABCMeta

class Algoritmo(metaclass=ABCMeta):
    def __init__(self, nombre, tarea, aprendizaje):
        self.nombre = nombre
        self. tarea = tarea
        self.aprendizaje = aprendizaje

class BaseClassifier(Algoritmo):
    def __init__(self, nombre, tarea, aprendizaje):
        super().__init__(nombre, tarea, aprendizaje)


print(issubclass(BaseClassifier, Algoritmo))

#################################################################################
#Ejercicio 7

# Escribe un script en Python para mostrar los
# distintos formatos de fecha y hora.
# a) Fecha y hora actuales
# b) Año actual
# c) Mes del año
# d) Número de la semana del año
# e) Día de la semana
# f) Día del año
# g) Día del mes
# h) Día de la semana

from datetime import datetime

def fecha_hora_actual(fecha):
    print("Fecha y hora actuales: ", fecha)

def año_actual(fecha):
    print("Año actual: ", fecha.strftime("%Y"))

def mes_actual(fecha):
    print("Mes del año: ", fecha.strftime("%m"))

def numero_semana(fecha):
    print("Número de la semana del año :", fecha.strftime("%U"))

def dia_semana(fecha):
    print("Día de la semana: ", fecha.strftime("%A"))

def dia_año(fecha):
    print("Día del año: ", fecha.strftime("%j"))

def dia_mes(fecha):
    print("Día del mes: ", fecha.strftime("%d"))

def dia_semana_numero(fecha):
    print("Día de la semana:", fecha.strftime("%w"))

print("Formatos de fecha y hora:")

fecha = datetime.now()

fecha_hora_actual(fecha)

año_actual(fecha)

mes_actual(fecha)

numero_semana(fecha)

dia_semana(fecha)

dia_año(fecha)   

dia_mes(fecha)

dia_semana_numero(fecha)


#################################################################################
#Ejercicio 8

# Escribe un programa en Python para convertir
# una cadena a datetime.
# INPUT: Jan 1 2014 2:43PM
# OUTPUT: 2014-07-01 14:43:00

from datetime import datetime

def convertir_cadena_a_datetime(cadena):
    formato = "%b %d %Y %I:%M%p"
    fecha_datetime = datetime.strptime(cadena, formato)
    return fecha_datetime

cadena_fecha = "Jan 1 2014 2:43PM"
fecha_convertida = convertir_cadena_a_datetime(cadena_fecha)
print("Fecha y hora convertida:", fecha_convertida)


#################################################################################
#Ejercicio 9

# Escribe un programa en Python para obtener la
# hora actual.

from datetime import datetime

hora_actual = datetime.now().time()
print("Hora actual:", hora_actual)

#################################################################################
#Ejercicio 10

# Escribe un programa en Python para restar cinco
# días a la fecha actual.


from datetime import datetime, timedelta

fecha_actual = datetime.now()
dias_a_restar = 5
nueva_fecha = fecha_actual - timedelta(days = dias_a_restar)

print("5 dias atras de la fecha actual: ")
print(nueva_fecha)

#################################################################################
#Ejercicio 11

# Escribe un programa en Python para convertir
# una cadena de marcas de tiempo unix en una
# fecha legible.
# INPUT Unix timestamp string: 1284105682
# OUTPUT: 2010-09-10 13:31:22

from datetime import datetime

def convertir_unix_a_fecha(unix_timestamp):
    timestamp = int(unix_timestamp)
    fecha_legible = datetime.fromtimestamp(timestamp)
    return fecha_legible

unix_timestamp = "1284105682"
fecha_convertida = convertir_unix_a_fecha(unix_timestamp)
print("Fecha y hora convertida:", fecha_convertida)
