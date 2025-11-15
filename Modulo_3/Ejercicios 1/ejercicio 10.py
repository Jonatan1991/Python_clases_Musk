#Ejercicio 10
class Estudiante:


    #ejercicio 10
    def __calificar_asistencia(self, asistencias):
        # Método privado para calcular la nota basada en asistencias
        for mes, num in asistencias.items():
            if num < 4:
                return 1
            if 4 <= num < 8:
                return 2
        return 3

    def obtener_nota_asistencia(self, asistencias):
       # Método público que utiliza el método privado
        return self.__calificar_asistencia(asistencias)

#instancia de la clase Estudiante
estudiante1 = Estudiante()


asistencias1 = {"Enero": 8, "Febrero": 8, "Marzo": 3}  # debería devolver 1, porque al menos 1 el valor es menor que 4
asistencias2 = {"Enero": 8, "Febrero": 8, "Marzo": 7}  # debería devolver 2, porque no hay ninguno menor que 4 pero hay al menos uno menor que 8
asistencias3 = {"Enero": 8, "Febrero": 8, "Marzo": 8}  # debería devolver 3, porque todos son mayores o igual que 8

print(f"Calificación asistencias1: {estudiante1.obtener_nota_asistencia(asistencias1)}")
print(f"Calificación asistencias2: {estudiante1.obtener_nota_asistencia(asistencias2)}")
print(f"Calificación asistencias3: {estudiante1.obtener_nota_asistencia(asistencias3)}")