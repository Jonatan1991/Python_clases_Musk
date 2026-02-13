with open("test.txt", 'w', encoding='utf-8') as f:
    f.write("texto 1\n")
    f.write("texto 2\n")
    f.write("texto 3\n")

f = open("test.txt", 'r', encoding='utf-8')

print(f.read(4))# leer los 4 primeros datos
print(f.read(4))# leer los siguientes 4 datos
print(f.read())# leer el resto hasta el final del archivo