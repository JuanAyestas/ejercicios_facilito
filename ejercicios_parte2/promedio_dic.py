calificaciones = {
  "Matematicas": 90,
  "Español": 82,
  "Economia": 70,
  "Programacion": 93,
  "Ingles": 98
}

resultado = 0
contador = 0

clases = list(calificaciones.keys())
print("Clases:")
for clase in clases:
  contador += 1
  print(clase)
print("----------")

print("Notas:")
notas = list(calificaciones.values())
for nota in notas:
  resultado += nota
  print(nota)
print("----------")

promedio = resultado / contador
print("El promedio es: {}".format(promedio))
