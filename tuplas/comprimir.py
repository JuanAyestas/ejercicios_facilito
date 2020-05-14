"""uno, dos, tres, *cuatro = tupla
print(uno)
print(dos)
print(tres)
print(cuatro)
"""

tupla = (1, 2, 3, 4, 5, 6)
tupla2 = (100, 200, 300, 400)
lista = [10, 20, 30, 40]
lista2 = [1000,2000,3000,4000]

resultado1 = zip(tupla, lista, tupla2, lista2)
resultado2 = zip(tupla, lista, tupla2, lista2)
lista3 = list(resultado1)
print(lista3)
tupla3 = tuple(resultado2)
print(tupla3)
