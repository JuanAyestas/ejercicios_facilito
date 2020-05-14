titulo = "Curso de Python miau"

#termina el ciclo
for caracter in titulo:
  if caracter == "P":
    break
  print(caracter)
print("--------")

#salta a la siguiente iteración
for caracter in titulo:
  if caracter == "P":
    continue
  print(caracter)
print("--------")
