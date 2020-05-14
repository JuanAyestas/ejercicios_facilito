animal = "Gato" #Variable global

def mostar_animal():
  global animal #define la variable dentro de la funcion como la global, sobreescribiendo la primera
  animal = "Perro" #Variable local = esta dentro de la funcion, solo accesible dentro de la misma
  print(animal)

mostar_animal()
print(animal)