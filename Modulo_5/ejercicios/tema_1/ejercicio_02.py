# Escribe una función para contar el número de
# líneas de un archivo de texto "historia.txt":
# Ejemplo: Si el archivo "story.txt" contiene las
# siguientes líneas
# Un niño está jugando allí.
# Hay un parque infantil.
# Un avión está en el cielo.
# El cielo es rosa.
# La contraseña puede contener letras y números.
# El resultado debe ser 5.

def contar_lineas():
    with open("Modulo_5/ejercicios/archivos/story.txt", "r", encoding="utf-8") as file:
        line_count = 0
        for line in file:
            line_count += 1
    return line_count

print(f"El archivo contiene {contar_lineas()} líneas.")