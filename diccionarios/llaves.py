diccionario = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}

#Usando método keys para obtener todas las llaves
resultado = diccionario.keys()
#resultado = tuple(resultado)
print(resultado)

#Usando values para obtener los valores de las llaves
resultado = diccionario.values()
#resultado = tuple(resultado)
print(resultado)

#retorna dict_items, las llaves con su valor correspondiente
resultado = diccionario.items()
#resultado = tuple(resultado)
print(resultado)
