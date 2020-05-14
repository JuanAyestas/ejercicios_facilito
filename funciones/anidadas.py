def comenzar_play_list(lista):

  def reproducir():
    """nonlocal lista""" #usado para definir una variable dentro de una funcion que sea global
    """lista = [1,2,3]""" #Lista de la primer def, es complematemente diferente de lista en esta def.
    for valor in lista:
      print("Se reproducira: {}".format(valor))
      
  reproducir()
  print(lista)

lista = []
counter = 0
print("""Introduzca el nombre de la cancion que quiere añadir 
  Con un maximo de 5 canciones por lista.""")
while counter < 5:  
  canciones = str(input("Nombre: "))
  lista.append(canciones)
  counter+=1
  
else:
  reproducir = comenzar_play_list(lista)