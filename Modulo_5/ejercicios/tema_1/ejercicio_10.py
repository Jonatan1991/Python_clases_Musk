# Escribe un programa en python para comprobar
# si un archivo especificado existe.

def comprobar_archivo():
    ruta = "Modulo_5/ejercicios/archisvos/"
    nombre_archivo = "story.txt"
    try:
         with open(ruta + nombre_archivo, "r", encoding="utf-8") as file:
            print(f"El archivo: {nombre_archivo} existe en la ruta: {ruta} y su contenido es:\n")
            for line in file:
                print(line.strip())
            
    except:
        print(f"el archivo: {nombre_archivo} no existe en la ruta: {ruta}")
              
comprobar_archivo()