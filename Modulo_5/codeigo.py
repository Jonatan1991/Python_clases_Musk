# 1. Abrir y Escribir en un Archivo (Modo 'w')
# Para abrir un archivo y escribir en él, utilizamos la función open().
#  El segundo argumento especifica el "modo" de apertura. El modo 'w' (write) abre el 
#  archivo para escritura. Si el archivo no existe, lo crea; si ya existe, borra su 
#  contenido y escribe desde cero.

# Es crucial cerrar el archivo después de terminar de escribir para asegurar que todos 
# los datos se guarden correctamente y liberar los recursos del sistema. Esto se hace 
# con el método .close().


# Abrir el archivo en modo escritura ('w')
file = open('mi_archivo.txt', 'w')

# Escribir contenido en el archivo
file.write('Hola, este es un archivo de texto.\n')
file.write('Esta es la segunda línea.\n')
file.write('Y esta es la tercera.')

# Cerrar el archivo
file.close()

print('Archivo "mi_archivo.txt" creado y escrito exitosamente.')


# 2. Abrir y Añadir Contenido a un Archivo (Modo 'a')
# Si quieres añadir contenido a un archivo existente sin borrar lo que ya tiene, 
# usa el modo 'a' (append). Si el archivo no existe, también lo creará.

# Abrir el archivo en modo añadir ('a')
file = open('mi_archivo.txt', 'a')

# Añadir más contenido
file.write('\nEsta línea se añadió al final.')

# Cerrar el archivo
file.close()

print('Contenido añadido a "mi_archivo.txt".')


# 3. La Mejor Práctica: Usar with open()
# Olvidar cerrar un archivo puede llevar a problemas, como la corrupción de datos o 
# la falta de liberación de recursos. La sentencia with open(...) as ...: es la forma 
# recomendada en Python para manejar archivos, ya que garantiza que el archivo se cierre
#  automáticamente cuando el bloque with finaliza, incluso si ocurre un error.
 
 # Usando 'with' para escribir
with open('otro_archivo.txt', 'w') as file:
    file.write('Este archivo se maneja con ')
    file.write('la sentencia with, ¡mucho mejor!\n')
    file.write('No necesito llamar a .close() explícitamente.')

print('Archivo "otro_archivo.txt" creado con')


# 4. Leer Contenido de un Archivo (Modo 'r')
# Para leer un archivo, usamos el modo 'r' (read). Hay varias maneras de leer el contenido:

# .read(): Lee todo el contenido del archivo como una sola cadena de texto.
# .readline(): Lee una sola línea del archivo.
# .readlines(): Lee todas las líneas del archivo y las devuelve como una lista de cadenas, donde cada cadena es una línea (incluyendo el carácter de nueva línea \n).
# Iterar sobre el objeto archivo: La forma más común y eficiente de leer un archivo línea 
# por línea.


# Leer todo el contenido con .read()
print('--- Lectura completa con .read() ---')
with open('mi_archivo.txt', 'r') as file:
    contenido_completo = file.read()
    print(contenido_completo)

# Leer línea por línea con .readline()
print('\n--- Lectura línea por línea con .readline() ---')
with open('mi_archivo.txt', 'r') as file:
    primera_linea = file.readline()
    segunda_linea = file.readline()
    print(f'Primera línea: {primera_linea.strip()}') # .strip() para quitar el salto de línea
    print(f'Segunda línea: {segunda_linea.strip()}')

# Leer todas las líneas en una lista con .readlines()
print('\n--- Lectura en lista con .readlines() ---')
with open('mi_archivo.txt', 'r') as file:
    lista_lineas = file.readlines()
    for i, linea in enumerate(lista_lineas):
        print(f'Línea {i+1}: {linea.strip()}')

# Iterar sobre el objeto archivo (la forma más común)
print('\n--- Iterando sobre el objeto archivo ---')
with open('mi_archivo.txt', 'r') as file:
    for i, linea in enumerate(file):
        print(f'Línea {i+1}: {linea.strip()}')
        
       