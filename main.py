print("Pagina 2022")
puntaje = 0
nombre =input("Ingresa tu nombre:\n")
print("Bienvenido",nombre,",comienzas con",puntaje,"puntos, porfavor realiza la siguiente encuesta.\n")



print("Pregunta 1: ¿Cual es la capital de Colombia?")
print("a) Bogota")
print("b) Cartagena")
print("c) Cali")
print("d) Medellin")

rpta1 = input("Ingresa una alternativa:")
while rpta1 not in("a","b","c","d","x"):
  rpta1 =input("Error, coloca una de las alternativas que estan en la encuesta ")

if rpta1 == "a":
  puntaje +=10
  print("Correcto",nombre,",tienes",puntaje,"puntos")
  

elif rpta1 == "b":
  print("Incorrecto",nombre,",tienes",puntaje,"puntos")

elif rpta1 == "x":
  print("Seleccionaste una alternativa secreta",nombre,", te damos 100 puntos\n")

elif rpta1 == "c":
  print("Incorrecto",nombre,",tienes",puntaje,"puntos")

else:
  print("Incorrecto",nombre,",tienes",puntaje,"puntos")


print("\nPregunta 2: ¿Cual es la capital de Venezuela?")
print("a) Lima")
print("b) Caracas")
print("c) Montevideo")
print("d) Berlin")

rpta2 = input("Ingresa una alternativa:")
while rpta2 not in("a""b""c""d"):
  rpta2 =input("Error, coloca una de las alternativas que estan en la encuesta ")

if rpta2 == "a":

  print("Incorrecto",nombre,",tienes",puntaje,"puntos")

elif rpta2 == "b":
  puntaje +=10
  print("Correcto",nombre,",tienes",puntaje,"puntos")

elif rpta2 == "c":
  print("Incorrecto",nombre,",tienes",puntaje,"puntos")

else:
  print("Incorrecto",nombre,",tienes",puntaje,"puntos")


print("\nGracias por participar,",nombre,",tu putaje final fue",puntaje,"puntos")
