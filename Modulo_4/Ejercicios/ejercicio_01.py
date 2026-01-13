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