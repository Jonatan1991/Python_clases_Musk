# Escriba una función en Python para leer líneas
# de un archivo de texto "notas.txt". Su función
# debe encontrar y mostrar la aparición de la
# palabra "el".

def buscar_palabra():
    with open("Modulo_5/ejercicios/notas.txt", "r", encoding="utf-8") as file:
        count = 0
        for linea in file:
            #Dicvide una cadena de texto en partes y devuelve varias lista de palabras divididas en lineas
            palabras = linea.split()
            for palabra in palabras:
                #pongo con el lower las palabras en minuscula para que me pueda reconecer el "El" primero 
                if palabra.lower() == "el":
                    count += 1
                    print(f"Aparición encontrada: {palabra}")

        print(f"Cantidad encontrada: {count}")

                
print("Método con split: ")    
print("este método no va a tomar una de las coincidencias porque tiene ,")
buscar_palabra()


#otro método pero con expresiones regulares Regex
import re

def buscar_palabra_2():
    palabra = "el"
    with open("Modulo_5/ejercicios/notas.txt", "r", encoding="utf-8") as file:
        texto = file.read()
        resultados = re.findall(palabra, texto, re.IGNORECASE)
        for resultado in resultados:
            print(f"Aparicion encontrada: {resultado}")
        
        print(f"Cantidad encontrada: {len(resultados)}")

print("\nMétodo con regex: ")
print("este metodo toma todas las coincidencias con el")
buscar_palabra_2()