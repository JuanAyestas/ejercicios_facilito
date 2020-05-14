lista = []
n = len(lista)

def resto_app():
  estara = input(
      "Ingrese el elemento que desee saber si está o no en la lista: ")
  resultado = estara in lista
  print("  El elemento '{}' se encuentra en la lista: {}".format(estara, resultado))

  print("  La lista actual es: {}".format(lista))
  
  insertar = input("Ingrese el elemento nuevo que desee agregar: ")
  lista.insert(n, insertar)
  print("El elemento {} se ha agregado a la lista.".format(insertar))
  print("  La lista actual es: {}".format(lista))

  borrar = input("Ingrese el elemento que desea borrar: ")
  lista.remove(borrar)
  print("El elemento {} se ha eliminado a la lista.".format(borrar))
  print("  La lista actual es: {}".format(lista))

  clear = input("Ingrese 'si' para vaciar la lista o 'no' para cancelar: ")
  if clear == "Si" or clear == "si":
    lista.clear()
    print("  La lista actual es: {}".format(lista))
  else:
    print("No hubo ningún cambio.")

variable = input("Ingrese algo a la lista: ")
while variable != "terminar" and variable != "Terminar":
  lista.append(variable)
  print("  La lista es: {}".format(lista))
  variable = input("Escriba algo o ingrese 'terminar' para finalizar: ")

elemento = input("Ingrese el elemente del cual quiere saber cuantos hay?\n")
contador = lista.count(elemento)
print("  En la lista hay: {} '{}'s".format(contador, elemento))

print("La lista actual es: {}".format(lista))
lugar = input("Ingrese el elemento cuya posición desee saber\n")
indice = lista.index(lugar)
print("  El elemento '{}' se encuentra en la posición: {}".format(lugar, indice))

longitud = len(lista)
print("  La lista tiene una longitud de: {} elemento/s".format(longitud))

"""menor = min(lista)
  print("  El elemento más pequeño (o primer elemento) de la lista es: {}".format(menor))
  mayor = max(lista)
  print("  El elemento más grande (o último elemento) de la lista es: {}".format(mayor))
"""

orden = input("De qué forma quiere ordenar la lista? (Mayor/menor/ninguna)\n")
if orden == "menor" or orden == "menor":
  lista.sort()
  print("  La lista actual es: {}".format(lista))
  resto_app()
elif orden == "mayor" or orden == "Mayor":
  lista.sort(reverse=True)
  print("  La lista actual es: {}".format(lista))
  resto_app()
else:
  resto_app()