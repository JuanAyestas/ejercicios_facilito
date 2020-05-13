import math
print("""
Medidas:
Centímetros(cm), Metros(m)
      """)
medida = input("Ingrese la medida a utilizar:\n")

altura = float(input("Ingrese la altura del edificio: "))
angulo = float(input("Ingrese el ángulo entre el edificio y el suelo: "))
radianes = math.radians(angulo)

if medida == "centimetros" or medida == "Centimetros" or medida == "cm" or medida == "CM":
  sombra = altura / math.sin(radianes)
  print("La sombra proyectada es de: %.5s %s" % (sombra, medida))
  
elif medida == "metros" or medida == "Metros" or medida == "m" or medida == "M":
  sombra = altura / math.sin(radianes)
  print("La sombra proyectada es de: %.5s %s" % (sombra, medida))
