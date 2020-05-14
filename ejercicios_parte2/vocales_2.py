#Mostrar en pantalla la frecuencia de aparición de vocales en una frase dada por el usuario.
#Ejemplo : 'Hola Mundo' salida : o=2, a=3, u=1

VOCALES = ["a","e","i","o","u"]
total_a = 0
total_e = 0
total_i = 0
total_o = 0
total_u = 0

oracion = str(input("Ingrese una oracion:\n"))
oracion_minus = oracion.lower()

for letra in oracion_minus:
  if 'a' in letra:
    total_a +=1
  if 'e' in letra:
    total_e +=1
  if 'i' in letra:
    total_i +=1
  if 'o' in letra:
    total_o +=1
  if 'u' in letra:
    total_u +=1

print("A = {}, E = {}, I = {}, O = {}, U = {}.".format(total_a, total_e, total_i, total_o, total_u))


