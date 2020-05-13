from datetime import date, datetime, timedelta

#week = timedelta(days=7.024)
#month = week * 4.34
#year = month * 12

def full_date(number):
  años = (abs(now.year - año - number))
  meses = (abs(now.month - mes))
  dias = (abs(now.day - dia))
  print("It's been {} years, {} months, y {} days since you were born.".format(
      años, meses, dias))
  detalle = input("""  If you want to know how old are you in months, weeks or days...
    Enter 'months', 'weeks' or 'days'\n""")
  while (detalle != "end" and detalle != "End"):
    if detalle == "months" or detalle == "Months":
      mes_total = (años * 12 + (now.month - mes))
      print("In total, your age is {} months old".format(mes_total))
    elif detalle == "weeks" or detalle == "Weeks":
      semanas_total = (round((años * 12 + (now.month - mes)) * 52, 2))
      print("In total, your age is {} weeks old".format(semanas_total))
    elif detalle == "days" or detalle == "Days":
      dias_total = (round(((años * 12 + (now.month - mes)) * 52) * 7.024, 2))
      print("In total, your age is {} days old".format(dias_total))
    else:
      print("Check if you entered the right input, then try again.")
    detalle = input("  Enter 'months', 'weeks', 'days' or 'end' to finish.\n")

def current_date_format(date):
    months = ("January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    messsage = "{} {} of {}".format(month, day, year)

    return messsage
  
nombre = input("Enter your name:\n")
print("Hi, {}, I hope you're okay, now...".format(nombre))

now = datetime.now()
año = int(input("Enter your year of birth: "))

if año >= 1900:
  print("""  January (1), February (2), March (3), April (4), May (5), June (6), 
  July (7), August (8), September (9), October (10), November (11), December (12)""")
  mes = int(input("Enter the number of your month of birth: "))
  if mes <= 12 and mes >= 1:
    dia = int(input("Enter your day of birth: "))
    if dia <= 31 and dia >= 1:
      date = datetime(año, mes, dia)
      print("You were born in {}".format(current_date_format(date)))
      if mes >= now.month:
        if dia >= now.day or dia <= now.day:
          full_date(1)
      elif mes <= now.month:
        if dia <= now.day or dia >= now.day: 
          full_date(0)
    else:
      print("Check if you entered a valid number, then try again.")
  else:
    print("Check if you entered a valid number, then try again.")
else:
  print("Check if you entered a valid number, then try again.")
