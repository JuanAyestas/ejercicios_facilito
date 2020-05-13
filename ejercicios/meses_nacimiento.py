from datetime import datetime
from datetime import date, datetime, timedelta

#week = timedelta(days=7.024)
#month = week * 4.34
#year = month * 12

def current_date_format(date):
    months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
              "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    messsage = "{} de {} del {}".format(day, month, year)

    return messsage

nombre = input("Escriba su nombre:\n")
print("Hola, {}, espero se encuentre bien. Ahora...".format(nombre))

now = datetime.now()
año = int(input("Introduzca su año de nacimiento: "))

if año >= 1900:
  print("""  Enero (1), Febrero (2), Marzo (3), Abril (4), Mayo (5), Junio (6), 
  Julio (7), Agosto (8), Septiembre (9), Octubre (10), Noviembre (11), Diciembre (12)""")
  mes = int(input("Introduzca el número del mes de nacimiento: "))
  if mes <= 12 and mes >=1:
    dia = int(input("Introduzca su día de nacimiento: "))
    if dia <= 31 and dia >=1:
      date = datetime(año, mes, dia)
      print("Nació el {}".format(current_date_format(date)))
      años = (abs(now.year - año - 1))
      meses = (abs(now.month - mes))
      dias = (abs(now.day - dia))
      print("Han transcurrido {} años, {} meses, y {} días desde su nacimiento".format(años, meses, dias))
      detalle = input("""  Si quiere saber su edad completa en meses, semanas o días...
  Ingrese 'meses', 'semanas' o 'dias'\n""")
      while (detalle != "Terminar" and detalle != "terminar" ):
        if detalle == "meses" or detalle == "Meses":  
          mes_total = (años * 12 + (now.month - mes))
          print("En total, su edad es de {} meses".format(mes_total))
        elif detalle == "semanas" or detalle == "Semanas":
          semanas_total = (round((años * 12 + (now.month - mes)) * 52, 2))
          print("En total, su edad es de {} semanas".format(semanas_total))
        elif detalle == "dias" or detalle == "Dias":
          dias_total = (round(((años * 12 + (now.month - mes)) * 52) * 7.024, 2))
          print("En total, su edad es de {} días".format(dias_total))
        else:
          print("Revise si ingresó correctamente la opción e inténtelo de nuevo.")
        detalle = input("  Ingrese 'meses', 'semanas', 'dias' o 'terminar' para finalizar\n")
    else:
      print("Revise si ingresó correctamente los números e inténtelo de nuevo.")
  else:
    print("Revise si ingresó correctamente los números e inténtelo de nuevo.")
else:
  print("Revise si ingresó correctamente los números e inténtelo de nuevo.")