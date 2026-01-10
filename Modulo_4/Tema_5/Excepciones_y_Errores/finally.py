try:
# Forzamos excepción
    x = 2/0
except:
# Se entra ya que ha habido una excepción
    print("Entra en except, ha ocurrido una excepción")
finally:
# También entra porque finally es ejecutado siempre 
    print("Entra en finally, se ejecuta el bloque finally")