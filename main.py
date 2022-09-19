import time
 

print("Pagina 2022")
magenta= '\033[35m'
reset= '\033[39m'
puntaje = 0
nombre = input("Ingresa tu nombre:\n")    
print("Bienvenido", nombre, ",comienzas con", puntaje,
      "puntos, porfavor realiza la siguiente encuesta.\n")

print("Pregunta 1: ¿Cual es la capital de Colombia?")
time.sleep(2)
print("a) Bogota")
time.sleep(2)
print("b) Cartagena")
time.sleep(2)
print("c) Cali")
time.sleep(2)
print("d) Medellin")

rpta1 = input("Ingresa una alternativa:")
while rpta1 not in ("a", "b", "c", "d", "x"):
    rpta1 = input(
        "Error, coloca una de las alternativas que estan en la encuesta ")

if rpta1 == "a":
    puntaje += 10
    print("Correcto", nombre, ",tienes", puntaje, "puntos")



elif rpta1 == "x":
  puntaje+=20
  print("Descubriste una alternativa secreta",nombre,",obtienes",puntaje,"puntos")
  
   



else:
    print("Incorrecto", nombre, ",tienes", puntaje, "puntos")

print(magenta,"\nPregunta 2: ¿Cual es la capital de Venezuela?")
print("a) Lima")
print("b) Caracas")
print("c) Montevideo")
print("d) Berlin",reset)

rpta2 = input("Ingresa una alternativa:")
while rpta2 not in ("a""b""c""d"):
    rpta2 = input(
        "Error, coloca una de las alternativas que estan en la encuesta ")

if rpta2 == "a":

    print("Incorrecto", nombre, ",tienes", puntaje, "puntos")

elif rpta2 == "b":
    puntaje += 10
    print("Correcto", nombre, ",tienes", puntaje, "puntos")

elif rpta2 == "c":
    print("Incorrecto", nombre, ",tienes", puntaje, "puntos")

else:
    print("Incorrecto", nombre, ",tienes", puntaje, "puntos")

print("\nGracias por participar,", nombre, ",tu putaje final fue", puntaje,
      "puntos")
