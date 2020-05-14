#Para usar un decorador, debe haber min 3 funciones
#a,b,c
#a(b)-> c

def decorador(funcion):
  def nueva_funcion(*args, **kwargs):
    print("Codigo aqui")
    resultado = funcion(*args, **kwargs)
    print("Codigo aqui, otra vez")
    return resultado
  
  return nueva_funcion

@decorador
def funcion_a_decorar():
  print("Esta es una funcion a decorar.")
funcion_a_decorar()

@decorador
def suma(val1, val2):
  return val1 + val2

funcion_a_decorar()
print("\n")
resultado = suma(20,30)
print(resultado)