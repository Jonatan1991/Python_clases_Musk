# Escriba una función en Python para leer líneas
# de un archivo de texto "notas.txt". Su función
# debe encontrar y mostrar la aparición de la
# palabra "el".

import re


class BuscarPalabras:
    def __init__(self, ruta_archivo):
        self.ruta = ruta_archivo

    def _leer_archivo(self):
        with open(self.ruta, "r", encoding="utf-8") as file:
            return file.read()

    def buscar_split(self, palabra):
        contenido = self._leer_archivo()
        count = 0

        for linea in contenido.split():
            # palabras = re.split(r"[ ,.;]+", linea)
            palabras = linea.split()
            for p in palabras:
                palabra_limpia = p.strip(",.;")
                if palabra_limpia.lower() == palabra.lower():
                    count += 1
                    print(f"Aparición encontrada: {palabra_limpia}")

        print(f"Cantidad encontrada (split): {count}")

    def buscar_regex(self, palabra):
        contenido = self._leer_archivo()
        patron = rf"\b{palabra}\b"
        resultados = re.findall(patron, contenido, re.IGNORECASE)

        for r in resultados:
            print(f"Aparición encontrada: {r}")

        print(f"Cantidad encontrada (regex): {len(resultados)}")


ejercicio_4 = BuscarPalabras("Modulo_5/ejercicios/archivos/notas.txt")

print("Método con split")
ejercicio_4.buscar_split("el")

print("\nMétodo con regex")
ejercicio_4.buscar_regex("el")
