#ejemplos
"""
Español, Matemáticas, Economía, Programación, Ingles
"""

nombre = input("Ingrese su nombre: ")
clases = int(input("Cuantas clases está cursando en este momento?\n"))
contador = 1
suma = 0
while contador <= clases:
  clase = input("Nombre de la materia {}: ".format(contador))
  nota = float(input("  Nota final en la clase de {}: ".format(clase)))
  if 100 >= nota >= 1:
    suma += nota
    contador += 1
  else:
    print("Introduzca una nota válida, entre 1 y 100.")

promedio = suma / clases
print("""Resultados:
  * Alumno: {}
  * Promedio de: {}""".format(nombre, promedio))
