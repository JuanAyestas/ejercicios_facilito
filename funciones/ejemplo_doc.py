def suma(a, b):
  """Función suma"""
  return a + b

def resta(a, b):
  """Función resta"""
  return a - b

def resta_negativos(a,b):
  """Resta de negativos"""
  return -(a-b)

opciones = {'a' : suma, 'b': resta}
print("Ingrese la opción deseada")

for opcion, funcion in opciones.items():
  mensaje = '{}) {}'.format(opcion, funcion.__doc__)
  print(mensaje)

opcion = input("Opción: ")
if opcion == "suma" or opcion == "Suma":
  print("Ingrese dos numeros para realizar la suma.")
  num1 = float(input("Primer numero: "))
  if num1 >= 1:
    num2 = float(input("Segundo numero: "))
    if num2 >= 1:
      resultado = suma(num1, num2)
      print(resultado)
      
elif opcion == "resta" or opcion == "Resta":
  print("Ingrese dos numeros para realizar la resta.")
  num1 = float(input("Primer numero: "))
  if num1 >= 1:
    num2 = float(input("Segundo numero: "))
    if num2 >= 1 and num2 <= num1:
      resultado = resta(num1,num2)
      print(resultado)
  elif num1 <= 0:
    num2 = float(input("Segundo numero: "))
    if num2 <= 0 and num2 <= num1:
      resultado = resta_negativos(num1,num2)
      print(resultado)
