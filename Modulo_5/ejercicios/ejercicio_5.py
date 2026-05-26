# Escriba una función display_words() en python
# para leer las lineas de un archivo de texto
# "story.txt", y mostrar aquellas palabras que
# tengan menos de 4 caracteres.
import re

#Como se haria normalmente
def display_words():
    with open("Modulo_5/ejercicios/story.txt", "r", encoding="utf-8") as file:
        count = 0
        for linea in file:
            palabras = linea.split()
            for palabra in palabras:
                palabra_limpia = palabra.strip(".,;:!?()[]{}\"'")
                if len(palabra_limpia) < 4:
                    print(f"palabra encontrada: {palabra_limpia}")
                    count += 1

        print(f"Total de palabras encontradas: {count}")

display_words()


#COn file.read() me quito un bucle de arriba
def display_words_2():
    with open("Modulo_5/ejercicios/story.txt", "r", encoding="utf-8") as file:
        texto = file.read()
        print(texto)

    palabras = texto.split()
    count = 0

    for palabra in palabras:
        palabra_limpia = palabra.strip(".,;:!?()[]{}\"'")
        if len(palabra_limpia) < 4:
            print("Palabra encontrada:", palabra_limpia)
            count += 1

    print("Total de palabras encontradas:", count)

display_words_2()

#respuesta hecha con expreciones regulares
def display_words_3():
    with open("Modulo_5/ejercicios/story.txt", "r", encoding="utf-8") as file:
        texto = file.read()

    # \b\w{1,3}\b → palabras de 1 a 3 caracteres
    palabras = re.findall(r"\b\w{1,3}\b", texto)

    for p in palabras:
        print("Palabra encontrada:", p)

    print("Total de palabras encontradas:", len(palabras))


display_words_3()