#Funcion para sumar un cantidad n de valores asignadas
def suma(nota,*args):
  total = 0
  print(nota)
  for valor in args:
    total += valor
  return total

def usuario_autenticados(**kwargs):
  return kwargs

def combinacion(requerido, *args, **kwargs):
  return(requerido,kwargs,args)
  
nota = str(input("Ingrese alguna nota: "))
resultado = suma(nota, 1, 2, 3, 5, 12, 32, 123)
print(resultado)

usuario = usuario_autenticados(Cato=True, Kuro=False)
print(usuario)

combinar = combinacion(nota, 10,20,30, valor_1=True, valor_2=False)
print(combinar)