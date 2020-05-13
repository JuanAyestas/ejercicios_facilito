import math

print("""
Tipos de triangulos:
Escaleno(Si tiene base y altura), Equilátero(Si tiene sólo 1 lado), Rectángulo(Si tiene 2 catetos y 1 angulo)""")
print("""
Medidas:
Centímetros(cm), Metros(m)
      """)
medida = input("Ingrese la medida a utilizar:\n")
inicio = input("Ingrese el tipo de triangulo:\n")


if inicio == "Escaleno" or inicio == "escaleno":
  base = int(input("Ingrese la base del triángulo: "))
  altura = int(input("Ingrese la altura del triángulo: "))
  area = (base * altura) / 2
  print("El área es: %.5s %s" % (area, medida))
  
elif inicio == "Equilatero" or inicio == "equilatero":
  lado = int(input("Ingrese un lado del triangulo: "))
  area = (((math.sqrt(3)) / 4) * (lado**2))
  print("El área es: %.5s %s" % (area, medida))
  
elif inicio == "Rectangulo" or inicio == "rectangulo":
  cateto1 = int(input("Ingrese el cateto a: "))
  cateto2 = int(input("Ingrese el cateto b: "))
  angulo = float(input("Ingrese el angulo en medio de ambos catetos: "))
  radian = math.radians(angulo)
  area = (0.5 * ((cateto1 * cateto2) * math.sin(radian)))
  print("El área es: %.5s %s" % (area, medida))
                
else:
  print("Opción incorrecta, intente de nuevo.")
