#lista = dinámica
lista = ["Curso", "Python", "Miau"]
#tupla = estática
tupla = ("Introducción", "Básico", "Listas", "Tuplas")

mensaje = input("Escriba el texto: ")

mensaje_2 = list(mensaje)
mensaje_3 = tuple(mensaje)
print(mensaje_2)
print(mensaje_3)

lista_2 = list(tupla)
tupla_2 = tuple(lista)
print(tupla_2)
print(lista_2)
