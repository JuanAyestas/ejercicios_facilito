def crear_usuario(nombre="Fulano", apellido="De Tal", edad="Viejito"):
  return {
    "nombre": nombre,
    "apellido": apellido,
    "nombre_completo": "{} {}".format(nombre, apellido),
    "edad": edad
  }

nombre = str(input("Ingrese su primer nombre: "))
apellido = str(input("Ingrese su primer apellido: "))
edad = int(input("Ingrese su edad: "))
if edad >= 1:
  datos = crear_usuario(nombre, apellido, edad)

print("""Si quiere ver sus datos, ingrese lo siguiente:
  'nombre', 'apellido', 'completo', 'edad'""")

opcion = str(input("Ingrese alguna de las opciones de arriba:\n"))
while opcion != "Terminar" and opcion != "terminar":
  if opcion == "nombre" or opcion == "Nombre":
    print("Su nombre es: {}.".format(datos["nombre"]))
    print("""  
  Si quiere ver el resto de sus datos, ingrese lo siguiente:
    apellido', 'completo', 'edad'
  Para finalizar, ingrese 'terminar'
""")
    opcion = str(input("Ingrese alguna de las opciones de arriba:\n"))
    
  elif opcion == "apellido" or opcion == "Apellido":
    print(" Su apellido es: {}.".format(datos["apellido"]))
    print("""
  Si quiere ver el resto de sus datos, ingrese lo siguiente:
    'nombre', 'completo', 'edad'
  Para finalizar, ingrese 'terminar'
  """)
    opcion = str(input("Ingrese alguna de las opciones de arriba:\n"))
    
  elif opcion == "completo" or opcion == "Completo":
    print("  Su nombre completo es: {}.".format(datos["nombre_completo"]))
    print("""
  Si quiere ver el resto de sus datos, ingrese lo siguiente:
    'nombre', 'apellido', 'edad'
  Para finalizar, ingrese 'terminar'
""")
    opcion = str(input("Ingrese alguna de las opciones de arriba:\n"))
    
  elif opcion == "edad" or opcion == "Edad":
    print("Su edad es: {}.".format(datos["edad"]))
    print("""
  Si quiere ver el resto de sus datos, ingrese lo siguiente:
    'nombre', 'apellido', 'completo'
  Para finalizar, ingrese 'terminar'
  """)
    opcion = str(input("Ingrese alguna de las opciones de arriba:\n"))
  else:
    print("Esa opcion no esta disponible. Intente otra vez. ")
    print("""  Si quiere ver sus datos, ingrese lo siguiente:
    'nombre', 'apellido', 'completo', 'edad'
  Sino, ingrese 'terminar' para finalizar.""")
    
    opcion = str(input("Ingrese alguna de las opciones de arriba:\n"))
