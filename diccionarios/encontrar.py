diccionario = {"a": 1, "b": 2, "c": 3, "a": 4}

#buscar valor en un diccionario
resultado = diccionario["a"]
print(resultado)

#si tal valor está dentro del diccionario, retorna bool
resultado = "a" in diccionario
print(resultado)

#retorna el valor dentro de esa llave del diccionario, retorna none si está vacío
resultado = diccionario.get("z", "No existe")
print(resultado)

#Si exite, retorna el valor, sino, crea uno nuevo con la llave dada y el valor
resultado = diccionario.setdefault("z", {"miau":12})
print(resultado)
print(diccionario)