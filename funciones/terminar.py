def funcion():
  print("Holi")
  print("Holi usted")
  return "miau"

resultado = funcion()
print(resultado)

def funcion(parametro):
  if parametro:
    return 100

resultado = funcion("")
if resultado:
  print("El resultado no es none.")
