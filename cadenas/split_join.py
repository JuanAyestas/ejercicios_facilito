#string a lista

lenguajes = "Python; Java; Ruby; PHP; Swift; JavaScript; C#; C; C++"
resultado = lenguajes.split("; ")
print(resultado)

#lista a string
nuevo_str = ", ".join(resultado)
print(nuevo_str)

#saltos de línea
texto = """Este
es 
un
mensaje
que
dice:

holi"""

resultado = texto.splitlines()
print(resultado)




