VOCALES = ["a","e","i","o","u"]
vacio = ""

oracion = str(input("Ingrese una oracion:\n"))
oracion_minus = oracion.lower()

for letra in oracion_minus:
  if letra not in VOCALES:
    vacio += letra

print("Oracion sin vocales: {}".format(vacio))