#rango empieza a contar desde 0 hasta el valor definido
for valor in range(10):
  print(valor)
print("------")

#definir donde comienza y que termine, incluso numeros negativos
for valor in range(1,10):
  print(valor)
print("------")

#incluye saltos
for valor in range(1,40,2):
  print(valor)
print("------")

#range y len
lista=[1,2,3,4,5,6]

for indice in range(len(lista)):
  print("Índice: {}, valor: {}".format(indice, lista[indice]))
print("------")

#Se puede añadir un punto de partida del indice, en este caso.
lista = [1, 2, 3, 4, 5, 6]

for indice, valor in enumerate(lista):
  print("Índice: {}, valor: {}".format(indice, valor))
print("------")
