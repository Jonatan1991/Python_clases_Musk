# Ejercicio 1

class Jet:
    def __init__(self, name, country):
        self.name = name
        self.origin = country

first_item = Jet("F-16", "USA")

print('Ejercicio 1')
print(f"Jet Name: {first_item.name}")

# ------------------------------------------------------------------
# Ejercicio 2

class Jet:
    def __init__(self, name, country):
        self.name = name
        self.origin = country

first_item = Jet("F-16", "USA")

second_item = Jet("SU33", "Russia")
third_item = Jet("AJS37", "Sweden")
fourth_item = Jet("Mirage2000", "France")
fifth_item = Jet("F14", "USA")
sixth_item = Jet("MiG-29", "USSR")
seventh_item = Jet("A-10", "USA")

print('Ejercicio 2')

print(f"Jet Name: {first_item.name}")



# ------------------------------------------------------------------
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

print('Ejercicio 3')
print(f"Jet Name: {fourth_item.name}, Cantidad: {fourth_item.cantidad}, Origin: {fourth_item.origin}")
print(f"Jet Name: {fifth_item.name}, Cantidad: {fifth_item.cantidad}, Origin: {fifth_item.origin}")


# ------------------------------------------------------------------
#Ejercicio 4

class Nobel:
    def __init__(self, category, year, winner):
        self.category = category
        self.year = year
        self.winner = winner

np2025 = Nobel("Peace", 2025, "Muhammad Yunus")

print('Ejercicio 4')
print(np2025.category, np2025.year, np2025.winner)

# ------------------------------------------------------------------
#Ejercicio 5

class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
#Instancia de la clase y asignacion de valores a los atributos creando asi un objeto

estudiante1 = Estudiante("Ana", 10, 5)
print('Ejercicio 5')
print(estudiante1.nombre, estudiante1.edad, estudiante1.grado)




# ------------------------------------------------------------------
#Ejercicio 6
class Estudiante:
    pass
print('Ejercicio 6')

# ------------------------------------------------------------------
#Ejercicio 7
class Estudiante:
    def __init__(self, grade = "primer grado"):
        self.grado = grade

    def media_notas(self, notas, grado):
        media = sum(notas) / len(notas)
        self.grado = grado
    
notas = [7, 8, 6, 5, 9, 6, 9, 2]
estudiante_1 = Estudiante()

#llamda a la funcion del programa principal que calcula la media y actualiza el grado
estudiante_1.media_notas(notas, "nuevo grado cambiado")

print('Ejercicio 7')
print(f'El nuevo grado del estudiante es: {estudiante_1.grado}')


# ------------------------------------------------------------------
#Ejercicio 8
class Estudiante:
    def __init__(self, grade = "primer grado"):
        self.grado = grade

    def media_notas(self, notas, grado):
        media = sum(notas) / len(notas)
        self.grado = grado
    
    @staticmethod
    def asignaturas_suspensas(asignaturas_notas):
        suspensas = []
        for asignatura, nota in asignaturas_notas.items():
            if nota <= 5:
                suspensas.append(asignatura)
        return suspensas
    

notas = [7, 8, 6, 5, 9, 6, 9, 2]
estudiante_1 = Estudiante()

#llamda a la funcion del programa principal que calcula la media y actualiza el grado
estudiante_1.media_notas(notas, "nuevo grado cambiado")

print('Ejercicio 8')
print(f'El nuevo grado del estudiante es: {estudiante_1.grado}')


notas_dic = {
    "Matemáticas": 4.5, 
    "Lengua": 6, 
    "Historia": 3, 
    "Inglés": 5
    }

print(f"Las asignaturas suspensas son: {Estudiante.asignaturas_suspensas(notas_dic)}")
    
# ------------------------------------------------------------------
#Ejercicio 9
class Estudiante:
    escuela = "Escuela 1"

    def __init__(self, grade):
        self.grado = grade
        

    @classmethod
    def actualizar_escuela(cls, nueva_escuela):
        cls.escuela = nueva_escuela

print('Ejercicio 9')
# vemos la escuela por defecto
print("Valor por defecto de escuela: ", Estudiante.escuela)  

# Actualizamos la escuela
Estudiante.actualizar_escuela("Escuela 2 que es el nuevo valor")

# Y mostramos la nueva escuela
print("Nuevo valor de escuela: ", Estudiante.escuela)  


# ------------------------------------------------------------------
#Ejercicio 10
class Estudiante:


    #ejercicio 10

    def __calificar_asistencia(self, asistencias):

        # metodo privado para extraer el valor minimo del diccionario y saber la clasificación de la asistencia
        asistencia_minima = min(asistencias.values())
        if asistencia_minima < 4:
            return 1
        if 4 <= asistencia_minima < 8:
            return 2
        else:
            return 3

    def obtener_nota_asistencia(self, asistencias):
       # Método público que utiliza el método privado
        return self.__calificar_asistencia(asistencias)

#instancia de la clase Estudiante
estudiante1 = Estudiante()

print('Ejercicio 10')
asistencias1 = {"Enero": 8, "Febrero": 8, "Marzo": 3}  # debería devolver 1, porque al menos 1 el valor es menor que 4
asistencias2 = {"Enero": 6, "Febrero": 8, "Marzo": 7}  # debería devolver 2, porque no hay ninguno menor que 4 pero hay al menos uno menor que 8
asistencias3 = {"Enero": 9, "Febrero": 8, "Marzo": 8}  # debería devolver 3, porque todos son mayores o igual que 8

print(f"Calificación asistencias1: {estudiante1.obtener_nota_asistencia(asistencias1)}")
print(f"Calificación asistencias2: {estudiante1.obtener_nota_asistencia(asistencias2)}")
print(f"Calificación asistencias3: {estudiante1.obtener_nota_asistencia(asistencias3)}")