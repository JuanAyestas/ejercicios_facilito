mensaje = "Este es un texto un poco grande porque blah blah blah blah blah blah blah blah"

#cuantas veces está cierto elemento en el str, si no está, retorna 0
resultado = mensaje.count("blah")
print(resultado)

#Uso de in or not in, retorna bool
resultado = "texto" in mensaje
print(resultado)

#uso de find, retorna la posición de la primera letra en el string, retorna -1 si no está
resultado = mensaje.find("texto")
print(resultado)

resultado = mensaje[resultado: resultado + len("texto")]
print(resultado)

#retorna valor bool, dependiendo si lo buscado se encuentra al inicio del mensaje
resultado = mensaje.startswith("Este")
print(resultado)

#retorna valor bool, dependiendo si lo buscado se encuentra al final del mensaje
resultado = mensaje.endswith("")
print(resultado)
