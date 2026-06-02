# Escribe un programa en python para calcular la
# frecuencia de todas las palabras de un archivo
# txt.

import re

class Frecuencia():
    def __init__(self, ruta_archivo):
        self.ruta = ruta_archivo


    def _leer_archivo(self):
        with open(self.ruta, "r", encoding="utf-8") as file:
            return file.read()
        
    
    def frecuencia_calculo(self):
        contenido = self._leer_archivo()
        frecuencia = {}
        for palabra in contenido.split():
            palabra_limpia = palabra.strip(".,;:!?()[]{}\"'")
            cant = re.findall(palabra_limpia, contenido, re.IGNORECASE)
            frecuencia[palabra] = len(cant)
        
        for palabra, cantidad  in frecuencia.items():
            print(f"la palabra {palabra} aparece {cantidad} veces en el texro")

            


ejercicio_9 = Frecuencia("Modulo_5/ejercicios/archivos/python.txt")


ejercicio_9.frecuencia_calculo()