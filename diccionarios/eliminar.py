diccionario = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
print(diccionario)

#cantidad de elementos en el diccionario
print(len(diccionario))

#usar palabra reservada del para eliminar una llave específica
del diccionario["a"]
print(diccionario)
print(len(diccionario))

#usar función pop para eliminar otra llave específca
valor = diccionario.pop("b")
print(valor)
print(diccionario)
print(len(diccionario))

#eliminar diccionario completamente
diccionario = {}
print(diccionario)
print(len(diccionario))

#eliminar diccionario completamente usando clear
diccionario.clear()
print(diccionario)
print(len(diccionario))
