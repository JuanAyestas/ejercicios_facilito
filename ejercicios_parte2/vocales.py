#Mostrar en pantalla la frecuencia de aparición de vocales en una frase dada por el usuario.
VOCALES = ["a","e","i","o","u"]
contador = 0

oracion = str(input("Ingrese una oracion:\n"))
oracion_minus = oracion.lower()

for letra in oracion_minus:
  if letra in VOCALES:
    contador +=1

print("La cantidad de vocales en la oracion es: {}".format(contador))