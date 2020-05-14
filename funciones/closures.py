def mostrar_mensaje(mensaje):
  mensaje = mensaje.title() #variable local
  def mostrar():
    print(mensaje)
  return mostrar

nueva_funcion = mostrar_mensaje("Holi usted")
nueva_funcion()