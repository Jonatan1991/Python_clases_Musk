# Escribe una función en Python para contar y
# mostrar el número total de palabras en un
# archivo de texto.

def contar_palabras():
    with open("Modulo_5/ejercicios/story.txt", "r") as file:
        content = file.read()
    words = content.split()
    return len(words)

print(f"El archivo contiene {contar_palabras()} palabras.")