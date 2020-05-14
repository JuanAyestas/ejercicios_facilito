lista = []
contador = 1

def mayor():
  mayor = max(lista)
  print("  El número mayor es: {}".format(mayor))

def menor():
  menor = min(lista)
  print("  El número menor es: {}".format(menor))

def suma_prom():
  cont = 0
  suma = 0
  for numero in lista:
    suma += numero
    cont += 1
  print("  La suma de todos los números es: {}.".format(suma))
  promedio = suma / cont
  print("El promedio es: {}".format(promedio))
  
numeros = int(input("Ingrese un número a la lista (No más de 10 números): "))
if numeros >= 1:
  while contador <= 10:
    lista.append(numeros)
    contador +=1
    print("  Lleva {} número/s.".format(contador-1))
    numeros = int(input("Ingrese otro número a la lista: "))
  else:
    print("  La lista es: {}".format(lista))
    mayor()
    menor()
    suma_prom()
else:
  print("  Ingrese solamente números positivos.")
