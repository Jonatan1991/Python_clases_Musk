#Ejercicio 8
class Estudiante:
    def __init__(self, grade):
        self.grado = grade

    def media_notas(self, notas):
        return sum(notas) / len(notas)
    
    @staticmethod
    def asignaturas_suspensas(asignaturas_notas):
        suspensas = []
        for asignatura, nota in asignaturas_notas.items():
            if nota <= 5:
                suspensas.append(asignatura)
        return suspensas
    

    
notas = [7, 8, 6, 5, 9, 6, 9, 2]
estudiante = Estudiante(5)
print(f'La media de las notas es: {estudiante.media_notas(notas)}, del grado: {estudiante.grado}')


notas_dic = {
    "Matemáticas": 4.5, 
    "Lengua": 6, 
    "Historia": 3, 
    "Inglés": 5
    }

print(f"Las asignaturas suspensas son: {Estudiante.asignaturas_suspensas(notas_dic)}")
    
