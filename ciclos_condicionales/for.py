numeros= [1,2,3,4,5,6,7,8,9,10]

for numero in numeros:
  print("{}".format(numero))
print("----------")
  
#si se usa for en un diccionario, sólo retorna las llaves y no los valores
diccionario = {"a": 1, "b":2}
for llave in diccionario:
  print(llave)
print("----------")

#retorna los objetos si hay un objeto que almacena información dentro de otro y otro y otro
valores =  ( (10,20), ["holi","usted"], (True,False))
for valor in valores:
  print(valor)
print("----------")

#si se añade otra variable, muestra los valores, si sabemos la cantidad de objetos dentro de los objetos
valores = ((10, 20), ["holi", "usted"], (True, False))
for valor, valor1 in valores:
  print(valor, valor1)
print("----------")
