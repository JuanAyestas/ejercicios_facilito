def saludo():
  print("Holi amorcini")

def crear_mensaje(nombre):
  return ("Holi {}, la quiero un monton.".format(nombre))

def suma():
  suma = 0
  for numero in numeros:
    suma += numero
  return ("  La suma de todos los números es: {}.".format(suma))

def decision():
  return ("un pico", "una ñiñeada", "que la achuche", "algo que usted elija")

nombre = str(input("Escriba su nombrecini, el suyo de usted:\n"))
mensaje =  crear_mensaje(nombre)
print(mensaje)

contador = 1
numeros = []
print("A continuacion, va a sumar owo (Solo 3 numeros, no se pase).")
while contador <= 3:
  valor = float(input("Ingrese el valor {}: ".format(contador)))
  if valor >= 1:
    contador += 1
    numeros.append(valor)
  else:
    print("Ingrese solo numeros positivos.")
else:
  resultado = suma()
  print(resultado)

op_1, op_2, op_3, op_4 = decision()
print("Y ahora, por ser bien wonita, que quiere?") 
print("  {}, {}, {}, o {}.".format(op_1, op_2, op_3, op_4))