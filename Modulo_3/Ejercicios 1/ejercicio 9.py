#Ejercicio 9
class Estudiante:
    escuela = "Escuela 1"

    def __init__(self, grade):
        self.grado = grade
        

    @classmethod
    def actualizar_escuela(cls, nueva_escuela):
        cls.escuela = nueva_escuela

# vemos la escuela por defecto
print("Valor por defecto de escuela: ", Estudiante.escuela)  

# Actualizamos la escuela
Estudiante.actualizar_escuela("Escuela 2 que es el nuevo valor")

# Y mostramos la nueva escuela
print("Nuevo valor de escuela: ", Estudiante.escuela)  
