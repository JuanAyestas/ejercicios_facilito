def cent_a_f(grados):
  return grados * 1.8 + 32
convertir = cent_a_f

print("Celcious a Fahrenheit.")

grados = float(input("Ingrese el numero de Celcious a convertir: "))
resultado = convertir(grados)
print("{} grados F.".format(resultado))

funcion = lambda grados=0 : grados * 1.8 + 32  #retorna un valor por default
resultado = funcion(grados)
print("{} grados F.".format(resultado))