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

#Clase Parent1
class Parent1():
    #Constructor
    def __init__(self, x):
        #Atributo
        self.x = x
    
    #Metodo display
    def display(self):
        print(f"IndisplaymethodofParent1: x = {self.x}")

#Clase Parent2
class Parent2():
    def __init__(self, y):
        self.y = y

    def display(self):
        print(f"IndisplaymethodofParent2: y = {self.x}")

#Clase Child que hereda de Parent1 y Parent2
class Child(Parent1, Parent2):
    #Constructor
    def __init__(self, x, y, z):
        #Llamada a los constructores de las clases padre
        Parent1.__init__(self, x)
        Parent2.__init__(self, y)
        self.z = z

    def display(self):
        print(f"IndisplaymethodofChild: x = {self.x}, y = {self.y}, z = {self.z}")

#Instancia de Child
obj = Child(10, 20, 30)
obj.display()

#Instancias de Parent1
obj1 = Parent1(12)
obj1.display()

#Instancias de Parent2
obj2 = Parent1(13)
obj2.display()

#################################################################################
#Ejercicio 3

# Crea una clase Car que herede de Vehicle y que
# sobreescriba los métodos max_speed() y
# change_gear(). Instancia dos objetos de cada
# clase y compruebaque la salida de cada método
# es distinta

# Clase base Vehicle
class Vehicle:
    #Constructor
    def __init__ (self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    #Metodo show
    def show(self):
        print('Details:', self.name, self.color, self.price)

    def max_speed(self):
        print('Vehicle max speed is 150')

    def change_gear(self):
        print('Vehicle change 6 gear')

# Nueva clase que hereda de la clase Vehicle
class Car(Vehicle):
    # Sobreescribiendo metodo max_speed
    def max_speed(self):
        print("Vehicle max speed is 240 Km/h")

     # Sobrescribiendo metodo change_gear
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

# Creando la interfaz formal
class Interfaz(metaclass=ABCMeta):

    #metodos abstractos
    @abstractmethod
    def preprocess_data(self, data, y):
        pass

    #metodos abstractos
    @abstractmethod
    def fit(self):
        pass

    @abstractmethod
    def predict(self):
        pass

# Implementando la interfaz en las clases SVM y DecisionTree
class SVM(Interfaz):

    #metodo preprocess_data
    def preprocess_data(self, data, y):
        self.data = data
        self.y = y

        print('Preprocessing data at SVM')

    def fit(self):
        print('Training at SVM')

    def predict(self):
        print('Evaluating at SVM')

# Implementando la interfaz en la clase DecisionTree
class DecisionTree(Interfaz):

    def preprocess_data(self, data, y):
        self.data = data
        self.y = y
        print('Preprocessing data at DecisionTree')

    def fit(self):
        print('Training at DecisionTree')

    def predict(self):
        print('Evaluating at DecisionTree')

# Probando las clases como lo dice el enunciado
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

# Creando la interfaz informal
class Interfaz:
    def preprocess_data(self):
        pass
    def fit(self):
        pass
    def predict(self):
        pass

# Implementando la interfaz en las clases SVM y DecisionTree
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

# Creando la clase virtual Algoritmo
class Algoritmo(metaclass=ABCMeta):
    #Constructor
    def __init__(self, nombre, tarea, aprendizaje):
        #Atributos
        self.nombre = nombre
        self. tarea = tarea
        self.aprendizaje = aprendizaje

# Creando la clase BaseClassifier que hereda de Algoritmo
class BaseClassifier(Algoritmo):
    #Constructor de la clase BaseClassifier
    def __init__(self, nombre, tarea, aprendizaje):
        # Llamada al constructor de la clase padre Algoritmo
        super().__init__(nombre, tarea, aprendizaje)

# Comprobando si Algoritmo es padre de BaseClassifier
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

# Funciones para mostrar los distintos formatos de fecha y hora

# a) Fecha y hora actuales
def fecha_hora_actual(fecha):
    print("Fecha y hora actuales: ", fecha)

# b) Año actual
def año_actual(fecha):
    print("Año actual: ", fecha.strftime("%Y"))

# c) Mes del año
def mes_actual(fecha):
    print("Mes del año: ", fecha.strftime("%m"))

# d) Número de la semana del año
def numero_semana(fecha):
    print("Número de la semana del año :", fecha.strftime("%U"))

# e) Día de la semana
def dia_semana(fecha):
    print("Día de la semana: ", fecha.strftime("%A"))

# f) Día del año
def dia_año(fecha):
    print("Día del año: ", fecha.strftime("%j"))

# g) Día del mes
def dia_mes(fecha):
    print("Día del mes: ", fecha.strftime("%d"))

# h) Día de la semana
def dia_semana_numero(fecha):
    print("Día de la semana:", fecha.strftime("%w"))

print("Formatos de fecha y hora:")

# Obteniendo la fecha y hora actual
fecha = datetime.now()

# Llamando a las funciones
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

# Función para convertir cadena a datetime
def convertir_cadena_a_datetime(cadena):
    # Definiendo el formato de la cadena
    formato = "%b %d %Y %I:%M%p"
    # Convirtiendo la cadena a datetime
    fecha_datetime = datetime.strptime(cadena, formato)
    return fecha_datetime

# Cadena de fecha a convertir
cadena_fecha = "Jan 1 2014 2:43PM"
# Llamando a la función
fecha_convertida = convertir_cadena_a_datetime(cadena_fecha)
print("Fecha y hora convertida:", fecha_convertida)


#################################################################################
#Ejercicio 9

# Escribe un programa en Python para obtener la
# hora actual.

from datetime import datetime

# Obteniendo la hora actual
hora_actual = datetime.now().time()
print("Hora actual:", hora_actual)

#################################################################################
#Ejercicio 10

# Escribe un programa en Python para restar cinco
# días a la fecha actual.


from datetime import datetime, timedelta

# Obteniendo la fecha actual
fecha_actual = datetime.now()

# Restando 5 días a la fecha actual
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

# Función para convertir cadena de marcas de tiempo unix a fecha legible
def convertir_unix_a_fecha(unix_timestamp):
    timestamp = int(unix_timestamp)
    fecha_legible = datetime.fromtimestamp(timestamp)
    return fecha_legible

unix_timestamp = "1284105682"
fecha_convertida = convertir_unix_a_fecha(unix_timestamp)
print("Fecha y hora convertida:", fecha_convertida)

#################################################################################
#Ejercicio 12

# Escribe un programa en Python para sumar 5
# segundos con la hora actual


from datetime import datetime, timedelta


hora_actual = datetime.now()

# Sumando 5 segundos a la hora actual
segundos_a_sumar = 5
nueva_hora = hora_actual + timedelta(seconds = segundos_a_sumar)

print("5 segundos adelante de la hora actual: ")
print(nueva_hora.time())

#################################################################################
#Ejercicio 13

# Escribe un programa en Python para obtener el
# número de la semana.

from datetime import datetime

# Función para obtener el número de la semana
def numero_semana():
    fecha = datetime.now()
    print("Número de la semana del año :", fecha.strftime("%U"))

numero_semana()

#################################################################################
#Ejercicio 14

# Escribe un programa en Python para seleccionar
# todos los domingos de un año determinado.


from datetime import datetime, timedelta

# Solución con más iteraciones y modificaciones:
def domingos_anno(anno):

    fecha = datetime(anno, 1, 1)
    #print(anno)
    #print(fecha.strftime("%Y"))
    #print(fecha.strftime("%A"))

    # Avanzar hasta el primer domingo del año
    while fecha.strftime("%Y") == str(anno):
        fecha = fecha + timedelta(days = 1)
        #comprobar si es domingo y mostramos la fecha
        if fecha.strftime("%A") == "Sunday":
            print(fecha.strftime("%A %d %B %Y"))


# domingos_anno(2025)


# Otra forma, pero con menos iteraciones y modificaciones:

def domingos_x_anno(anno):
    fecha = datetime(anno, 1, 1)

    # Avanzar hasta el primer domingo del año, weekday() es otra forma de obtener el dia de la semana como el strftime("%A")
    while fecha.weekday() != 6:
        #incrementar un dia hasta encontrar el domingo
        fecha += timedelta(days=1)
        
    # Iterar a través del año de 7 en 7 para que tenga menos iteraciones y mostrampos todos los domingos
    while fecha.year == anno:
        print(fecha.strftime("%A %d %B %Y"))
        fecha += timedelta(days=7)
            

domingos_x_anno(2026)

#################################################################################
#Ejercicio 15

# Escribe un programa en Python para contar el
# número de lunes del primer día del mes desde
# 2015 hasta 2016.


from datetime import datetime, timedelta

# Función para contar el número de lunes del año 2015
def cantidad_lunes():

    #creamos contador y lo inicializamos a 0
    count_lunes = 0
    #creamos la fecha inicial
    fecha = datetime(2015, 1, 1)

    # Iteramos desde el 1 de enero de 2015 hasta el 31 de diciembre de 2015
    while fecha.year < 2016:
        if fecha.weekday() == 0:
            count_lunes += 1
        fecha += timedelta(days=1)

    return count_lunes


print("La cantidad de lunes que tiene el año 2015 es: ", cantidad_lunes(), "lunes")


#################################################################################
#Ejercicio 16

# Escribe un programa en Python para crear 12
# fechas fijas a partir de una fecha especificada en
# un periodo determinado. La diferencia entre dos
# fechas será de 20.

from datetime import datetime, timedelta

def fechas():

    #creando la fecha especifica  
    fecha_especifica = datetime(2000, 2, 4)
    count = 1

    # Iteramos 12 veces sumando 20 dias a la fecha especifica para obtener las 12 fechas
    while count <= 12:
        print(fecha_especifica.strftime("%A %d %B %Y"))
        fecha_especifica += timedelta(days = 20)
        count += 1


print(fechas())

# Respuesta con return y una lista, porque al final me devuelve un none con la respuesta anterior
def fechas_2():

    fecha_especificada = datetime(2003, 3, 28)
    count = 0
    #creando la lista vacia
    lista_fechas = []

    # Iteramos 12 veces sumando 20 dias a la fecha especifica para obtener las 12 fechas
    while count <= 11:
        lista_fechas.append(fecha_especificada.strftime("%A %d %B %Y"))
        fecha_especificada += timedelta(days=20)
        count += 1

    #retornando la lista de fechas
    return lista_fechas

# Imprimiendo las fechas generadas
print("\n")
print("Segunda forma de mostrar las fechas:")
for fecha in fechas_2():
    print(fecha)

#################################################################################
#Ejercicio 17

# Implementa una función generadora que dadas
# dos listas del mismo tamaño, devuelva la
# multiplicación entre los elementos de cada una,
# el primer elemento de la lista 1 por el primero de
# la lista 2, el segundo con el segundo y así
# sucesivamente. Sigue la siguiente estructura:

# def prod(l1, 12):

# except StopIteration:
# pass
# return solution

# Añadiendo el bloque except capturamos la
# excepción de Stop Iteration que se produce al
# acabar de leer todos los elementos de un
# generador.

# funcion generadora que devuelve la multiplicacion entre los elementos de cada lista
def prod(l1, l2):
    #iteradores para cada lista, el iter nos permite recorrer cada lista elemento por elemento y asi poder utilizar el next
    it1 = iter(l1)
    it2 = iter(l2)

# Creamos un bloque try para capturar la excepcion 
    try:
        # buclme que se detendra al lanzar la excepcion de StopIteration cuando se acaben los elementos de las listas
        while True:
           solution =  yield next(it1) * next(it2)
    except StopIteration:
        pass
    return solution

list_1 = [1, 2, 3, 4, 5, 6, 7]
list_2 = [2, 4, 6, 7, 9, 3, 1]

resultado = prod(list_1, list_2)

for i in resultado:
    print(i)


#################################################################################
#Ejercicio 18

# Implementa un generador, que dado un entero n,
# genere n números aleatorios. Puedes usar el
# método random de la librería random para
# generar números aleatorios.

import random

#funcion generadora
def numeros_random(n):
    #  iteramos n veces para generar n numeros aleatorios
    # el _ es indica que no se va a usar la variable de iteración, es una conversion
    for _ in range(n):
       
        # yield random.random() # asi me devuelve numeros decimales random
       
        yield random.randint(1, 100) #asi me devuelve nuemros random enteros

numeros = numeros_random(7)
for num in numeros:
    print(num)


#################################################################################
#Ejercicio 19

# Implementa un generador de Fibonacci que
# genere n números de la secuencia de Fibonaccі,
# que tiene la forma:
# 0, 1, 1, 2, 3, 5, 8, 13, ...
# Cuyos dos primeros valores son 0 y 1 por
# definición y el resto se calculan sumando los dos
# últimos valores de la sucesión.

#funcion generadora de Fibonacci
#fibonacci es una sucesion infinita
def numeros_fibonacci(nums):
    #inicializamos los dos primeros valores de la sucesion
    x, y = 0, 1
    # iteramos nums veces para generar los numeros de la sucesion
    for _ in range(nums):
        # el yiel es como un return pero para generadores, devuelve el valor de x
        yield x
        # actualizamos los valores de x e y, el nuevo valor de x es el valor de y y el nuevo valor de y es la suma de x e y
        x, y = y, x+y

for num in numeros_fibonacci(10):
    print(num)


#################################################################################
#Ejercicio 20

# Implementa un generador, que dado un entero n,
# imprima todos los números inferiores a n
# multiplicados por dos.

# Solucion 1
def generador(n):
    for x in range(n):
       
       yield x * 2

numeros = generador(5)
for x in numeros:
    print(x)


# Solucion 2 por si el resultado de la multiplicacion es el que debe ser menor que el numero entero n
def generador_2(n):
    for x in range(n):
        num = x * 2
        if num < n:
            yield num
print("\n")
print("Solucion 2")
for i in generador_2(5):
    print(i)


#################################################################################
#Ejercicio 21

#Implementa un generador, que dado un entero n,
#genere n número senares.


import random

# funcion generadora que devuelve n numeros senares, 
# si el numero generado es par se le resta 1 para convertirlo en impar
def numeros_senares(n):
    for _ in range(n):
        numero = random.randint(1, 99)
        if numero % 2 != 0:
            yield numero
        else:
            numero = numero - 1
            yield numero

for impar in numeros_senares(10):
    print(impar)


#################################################################################
#Ejercicio 22

# Crea una función que genere una excepción e
# imprima su tipo, los argumentos de la excepción
# y su mensaje de error.

def suma(x, y):
    try:
        result = x + y
        return result
    # Capturamos cualquier tipo de excepción que se pueda generar
    except Exception as error:
        print("Type: ", type(error))
        print("Argumentos: ", error.args)
        print("Mensaje de error: ", str(error))


print(suma(1, "Hola"))

#################################################################################
#Ejercicio 23

# Crea una función que compute la diferencia
# entre dos enteros. En caso de que la diferencia
# sea negativa genera una excepción inventada
# por ti que informe sobre ello. Por ejemplo. la
# excepción podría llamarse
# NegativeDifferenceException.


# Excepción personalizada NegativeDifferenceException
class NegativeDifferenceException(Exception):
    pass


def diferencia(a, b):
    resultado = a - b
    if resultado < 0:
        # Si la diferencia es negativa, lanzamos la excepción personalizada con un mensaje de error
        raise NegativeDifferenceException(f"La diferencia es negativa: {resultado}")
    return resultado

try:
    print(diferencia(3, 10))   # Lanza excepción
except NegativeDifferenceException as error:
    print("Error:", error)


#################################################################################
#Ejercicio 24

# Crea una función que calcule la división entre
# dos números. Debe imprimir el mensaje 'Los
# parámetros deben ser número enteros' cuando
# se genera una excepción de tipo y 'El divisor no
# puede ser 0' cuando se genera un
# zerodivisionerror.


def division(x, y):
    try: 
        result = x / y
        return result
    # Capturamos la excepción de tipo TypeError que se puede generar si los parámetros no son números enteros
    except TypeError:
        print("Los parámetros deben ser números enteros")
        # Capturamos la excepción de tipo ZeroDivisionError que se puede generar si el divisor es 0
    except ZeroDivisionError:
        print("El divisor no puede ser 0")
    

print(division(4, "hola"))
print(division(4, 0))
print(division(4, 2))

#################################################################################
#Ejercicio 25

# Añade a la función anterior, un mensaje que se
# imprima al final de la ejecución de la función
# independientemente de si se ha generado
# excepción o no.



def division(x, y):
    try: 
        result = x / y
        return result
    except TypeError:
        print("Los parámetros deben ser números enteros")
    except ZeroDivisionError:
        print("El divisor no puede ser 0")
    # El bloque finally se ejecuta siempre, independientemente de si se ha generado una excepción o no
    finally:
        print("Este es el último ejercicio para finalizar el modulo 4")

print(division(4, "hola"))
print(division(4, 0))
print(division(4, 2))














