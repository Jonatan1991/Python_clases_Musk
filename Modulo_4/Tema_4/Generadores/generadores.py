def funcion_generadora():
    print("GENERADOR: Se va a generar un PRIMER dato")
    yield "valorGeneradol"

    print("GENERADOR: Se va a generar un SEGUNDO dato")
    yield "valorGenerado2"

    print("GENERADOR: Se va a generar un TERCER dato")
    yield "valorGenerado3"

    print("GENERADOR: Termina y lanzará automáticamente la excepción StopIteration")

generador = funcion_generadora()

for elemento in generador:
    print(elemento)