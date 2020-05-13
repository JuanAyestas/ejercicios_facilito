#vel_luz = 300.000km/h
#distancia1 = 102, 000, 000km
#distancia2 = 59, 000, 000km

print("Cuanto tardaría en moverse la luz de Tierra a Marte?")
print("""
Tomando en cuenta si está en el:
Afelio o Perihelio
""")
vel_luz = 300000

inicio = input("Ingrese alguna de las dos opciones:\n")
if inicio == "afelio" or inicio == "Afelio":
  distancia = 102000000
  tiempo = distancia / vel_luz
  print("Tardaría en llegar desde la tierra a marte" +
        " " + ("%.6s" % tiempo) + " " + "segundos")
  
elif inicio == "perihelio" or inicio == "Perihelio":
  distancia = 59000000
  tiempo = distancia / vel_luz
  print("Tardaría en llegar desde la tierra a marte" +
        " " + ("%.6s" % tiempo) + " " + "segundos")

else:
  print("Opcion incorrecta, intente de nuevo.")
