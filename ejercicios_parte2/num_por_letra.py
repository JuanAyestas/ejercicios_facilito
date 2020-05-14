from string import ascii_lowercase

def alphabet_position(text):
  text = text.lower()
  numbers = [LETRAS[character] for character in text if character in LETRAS]

  return ''.join(numbers)

LETRAS = {letter: str(index)
           for index, letter in enumerate(ascii_lowercase, start=1)}

oracion = str(input("Ingrese una oración o palabra\n"))
resultado = alphabet_position(oracion)
print("{}".format(resultado))



    





