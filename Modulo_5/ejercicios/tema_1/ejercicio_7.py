# Escribe un programa en Python para generar 26
# archivos de texto llamados A.txt, B.txt, y así
# sucesivamente hasta Z.txt


import string
def archivos():
    # string.ascii_uppercase Es una cadena con todas las letras mayúsculas del alfabeto
    for letra in string.ascii_uppercase:
        nombre_archivo = f"{letra}.txt"
        ruta = "Modulo_5/ejercicios/archivos_generados/" + nombre_archivo
        
        with open(ruta, "w", encoding="utf-8") as file:
            file.write(f"Este es el archivo {nombre_archivo}\n")

archivos()