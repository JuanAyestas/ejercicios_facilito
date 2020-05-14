texto = "Curso de Python miau, Python básico   "

#1ra letra en mayúscula
resultado = texto.capitalize()
print(resultado)

#cambia todas las mayúsculas a minúsculas y viceversa
resultado = texto.swapcase()
print(resultado)

#todas las letras a mayúscula
resultado = texto.upper()
print(resultado)
#valor bool si el str está todo en mayúscula
print(resultado.isupper())

#todas las letras a minúscula
resultado = texto.lower()
print(resultado)
#valor bool si el str está todo en minúscula
print(resultado.islower())

#formatea el str para que sea título
resultado = texto.title()
print(resultado)

#reemplaza una palabra con otra
resultado = texto.replace("Python", "gatos", 1)
print(resultado)

#retorna string sin espaciado al inicio o final
resultado = texto.strip()
print(resultado)
