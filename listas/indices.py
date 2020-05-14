"""
  Estas son las formas en las cuales podemos crear una nueva lista (sublistas) a partir de otra.
  [:] Todos los elementos.
  [desde:] Todos los elementos desde el índice establecido(desde).
  [:hasta] Todos los elementos desde el índice cero hasta el índice establecido(hasta).
  [desde:hasta] Todos los elementos de un rango de índices.
  [desde:hasta:step] Todos los elementos de un rango de índices con saltos.
  De igual forma, este listado es aplicable a las tuplas y los strings.
"""

cursos = ["Python", "Django", "Flask",
          "C", "C#", "C++", "Java", "Php"]
sub = cursos[:]
print(sub)
