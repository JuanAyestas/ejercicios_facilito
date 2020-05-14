calificación = int(input("Ingrese la calificación de su clase: "))

color = "Verde" if calificación >= 7 else "Rojo"
if calificación >= 1 and calificación <= 10:
  print("  La clasificación es: {} ({})".format(calificación, color))
else:
  print("  Ingrese un nùmero del 1 al 10. Ingresó: {}".format(calificación))
