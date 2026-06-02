# Escribe un programa en python para añadir
# texto a un archivo y mostrar el texto en
# python.txt


def anadir_texto():
    nombre_archivo = "python.txt"
    ruta = "Modulo_5/ejercicios/archivos_generados/" + nombre_archivo
    texto = "Hola mundo\n"

    with open(ruta, "a", encoding="utf-8") as file:
        file.write(texto)

    with open(ruta, "r", encoding="utf-8") as file:
        print(file.read())

anadir_texto()