lista = []
contador = 0

def palindrome():
  for palabras in lista:
    pal = palabras.casefold()
    rev_pal = reversed(pal)
    if list(pal) == list(rev_pal):
      print("La palabra: {} es un palíndromo.".format(pal))
      print("------")
    else:
      print("La palabra: {} no es un palíndromo.".format(pal))
      print("------")

print("Bienvenido al verificador de Palíndromos, por favor...")
while contador <=5:
  palabras = str(input("  Ingrese una palabra: "))
  lista.append(palabras)
  contador +=1
else:
  print("  Las palabras que ingresó fueron:\n{}".format(lista))
  palindrome()
