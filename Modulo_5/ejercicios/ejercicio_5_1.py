# Escriba una función display_words() en python
# para leer las lineas de un archivo de texto
# "story.txt", y mostrar aquellas palabras que
# tengan menos de 4 caracteres.

import re

class palabras_menores_numero:
    def __init__(self, ruta_archivo):
        self.ruta = ruta_archivo

    def _leer_archivo(self):
        with open(self.ruta, "r", encoding="utf-8") as file:
            return file.read()

    #Como se haria normalmente
    def display_words(self, cant_caracteres):
        contenido = self._leer_archivo()
        count = 0
       
        for palabra in contenido.split():
            palabra_limpia = palabra.strip(".,;:!?()[]{}\"'")
            if len(palabra_limpia) <= cant_caracteres:
                print(f"palabra encontrada: {palabra_limpia}")
                count += 1

        print(f"Total de palabras encontradas: {count}")


#respuesta hecha con expreciones regulares
    def display_words_2(self, cant_caracteres):
        contenido = self._leer_archivo()

        # \b\w{1,3}\b → palabras de 1 a 3 caracteres
        palabras = re.findall(rf"\b\w{{1,{cant_caracteres}}}\b", contenido)

        for p in palabras:
            print("Palabra encontrada:", p)

        print("Total de palabras encontradas:", len(palabras))

ejercicio_5 = palabras_menores_numero("Modulo_5/ejercicios/archivos/story.txt")


ejercicio_5.display_words(3)

ejercicio_5.display_words_2(3)