# Escribe una función en python para leer el
# contenido de un archivo de texto "poema.txt"
# línea por línea y mostrar el mismo en pantalla.


def leer_poema():
    with open("Modulo_5/ejercicios/poema.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line.strip())
            
leer_poema()