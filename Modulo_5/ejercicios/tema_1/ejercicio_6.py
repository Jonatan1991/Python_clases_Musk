# Un archivo de texto llamado "materia.txt"
# contiene algún texto, que necesita ser mostrado
# de manera que cada carácter siguiente esté
# separado por un símbolo "#". Escriba una
# definición de función para hash_display() en
# Python que muestre todo el contenido del
# archivo matter.txt en el formato deseado.
# Ejemplo : Si el archivo materia.txt tiene el
# siguiente contenido almacenado :
# EL MUNDO ES REDONDO
# La función hash_display() debería mostrar el
# siguiente contenido :
# T#H#E# #W#O#R#L#D# #I#S# #R#O#U#N#D#

import re

class TransformarTexto():
    def __init__(self, ruta_archivo):
        self.ruta = ruta_archivo

    def _leer_archivo(self):
        with open(self.ruta, "r", encoding="utf-8") as file:
            return file.read()

    def hash_display(self):
        contenido = self._leer_archivo()
        for character in contenido:
            print(f"{character}#", end="") #end evita el salto de linea

    def hash_display_join(self):
        contenido = self._leer_archivo()
        resultado = "#".join(contenido)
        print(resultado)

    def hash_display_re(self):
        contenido = self._leer_archivo()
        resultado = re.sub(r"(.)", r"\1#", contenido)
        print(resultado)


ejercicio_6 = TransformarTexto("Modulo_5/ejercicios/archivos/matter.txt")


ejercicio_6.hash_display()
ejercicio_6.hash_display_join()
ejercicio_6.hash_display_re()