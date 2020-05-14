lista = []

print("  Puede ingresar 5 numeros.")
counter = 0
numero = 0
while counter < 5:
  numero = float(input("Introduzca un numero: "))
  if numero >= 1:
    lista.append(numero)
    counter+=1
else:
  resultado = map(lambda numero: numero * numero, lista)
  lista_resultado = list(resultado)
  for resultado in lista_resultado:
    print("El cuadrado es: {}".format(resultado))
    