import math

print("""
Medidas:
Centímetros(cm), Metros(m)
      """)
medida = input("Ingrese la medida a utilizar:\n")

radio = float(input("Ingrese el radio de la llanta: ")) #cm
distancia = float(input("Ingrese la distancia a recorrer: ")) #m

if medida == "centimetros" or medida == "Centimetros" or medida == "cm" or medida == "CM":
  dist_vuelta = (2 * math.pi * radio)
  print("Distancia por vuelta: %.5s %s" % (dist_vuelta, medida))
  num_vueltas = 1 * (distancia) / dist_vuelta
  print("El numero de vueltas que da en %s %s es: %.6s" % (distancia, medida, num_vueltas))
  
elif medida == "metros" or medida == "Metros" or medida == "m" or medida == "M":
  dist_vuelta = (2 * math.pi * radio)
  print("Distancia por vuelta: %.5s %s" % (dist_vuelta, medida))
  num_vueltas = 1 * (distancia) / dist_vuelta
  print("El numero de vueltas que da en %s %s es: %.6s" % (distancia, medida, num_vueltas))



