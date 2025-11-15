#Ejercicio 7
class Estudiante:
    def __init__(self, grade):
        self.grado = grade

    def media_notas(self, notas):
        return sum(notas) / len(notas)
    
notas = [7, 8, 6, 5, 9, 6, 9, 2]
estudiante = Estudiante(5)
print(f'La media de las notas es: {estudiante.media_notas(notas)}, del grado: {estudiante.grado}')