nombre = input("Cuál es tu nombre?\n")
edad = int(input("Qué edad tienes?\n"))
peso = float(input("Cuál es tu peso?\n"))
autorizado = input("Estás autorizado? si/no\n") == "Si"

print("Hola,", nombre)
print("Tienes" + " " + str(edad) + " " + "años de edad")
print("Y tienes un peso de:", peso)
print("Autorización aceptada?", autorizado)
