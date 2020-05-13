edad1 = int(input("Ingrese la primera edad:\n"))
edad2 = int(input("Ingrese la segunda edad:\n"))

if edad1 == edad2:
  comparar = edad1 == edad2
  print("Es %s = %s? %s" % (edad1, edad2, comparar))

elif edad1 > edad2:
  comparar = edad1 > edad2
  print("Es %s mayor que %s? %s" % (edad1, edad2, comparar))

elif edad1 < edad2:
  comparar = edad1 < edad2
  print("Es %s menor que %s? %s" % (edad1, edad2, comparar))
