def tabla_multiplicar(numero, maximo=10):
  for posicion in range(1, maximo+1):
    yield numero * posicion, numero, posicion

peticion = int(input("Ingrese el numero del cual quiera saber su tabla: "))
veces = int(input("Ingrese el numero de veces que quiera repetir el numero  {}: ".format(peticion)))
print("Tabla del {}:".format(peticion))
for resultado, numero, posicion in tabla_multiplicar(peticion, veces):
  print("{} x {} = {}".format(numero, posicion, resultado))