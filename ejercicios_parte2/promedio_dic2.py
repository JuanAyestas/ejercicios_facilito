import operator

calificaciones = {
  "Programacion": 93,
  "Economia": 70,
  "Español": 82,
  "Ingles": 98,
  "Matematicas": 90
}
clases = tuple(calificaciones.items())
for clase, nota in clases:
  print("Clase: {}, nota: {}".format(clase, nota))
print("--------")

ordenado = sorted(calificaciones.items(), key=operator.itemgetter(1))
dict_ordenado = dict(ordenado)
keys = list(dict_ordenado.keys())
values = list(dict_ordenado.values())

print("La clase {}, tiene la nota más alta con {}.".format(keys[-1], values[-1]))