print("Pagina 2022")
nombre = input("Coloca tu nombre:")

puntaje = 0


print("Bienvenido", nombre,",tienes",puntaje,"puntos,resuelve las siguientes preguntas de la encuesta:\n ")


print("Pregunta1: ¿Cual es la capital del Peru?")
print("a) Tocata")
print("b) Breña")
print("c) lima")
print("d) breña\n")

puntaje = 0
rpta = input("La respuesta es:")

while rpta not in("a","b","c","d","x"):
  rpta = input("Coloca una alternativa valida\n")

if rpta == "x":
  puntaje += 100
  print(nombre,",encontraste un mensaje secreto, felicidades, te damos una puntuacion especial!!")

elif rpta == "a":
  print("Incorrecto", nombre,",la alternativa",rpta,"no es la correcta")
  print("totalmente incorrecto")
   

elif rpta == "b":
  print("Incorrecto", nombre,",la alternativa",rpta,"no es la correcta")

elif rpta == "c":
  puntaje+=10
  print("Correcto", nombre,",la alternativa",rpta," es la correcta")
  print("Sumaste",puntaje,"puntos")

else :
  
 print("inCorrecto", nombre,"la alternativa",rpta,"es la respuesta incorrecta\n")


print("pregunta 2: ¿De que color es el sol?")
print("a) azul")
print("b) amarillo")
print("c) negro")
print("d) morado\n")

rpta = input("La respuesta es:")

while rpta not in("a","b","c","d","x"):
  rpta = input("Coloca una alternativa valida\n")

if rpta == "a":
  print("Incorrecto", nombre,",la alternativa",rpta,"no es la correcta")


elif rpta == "b":
  puntaje+=10
  print("Correcto", nombre,",la alternativa",rpta,"es la correcta")
  

elif rpta == "c":
    print("Incorrecto", nombre,",la alternativa",rpta," no es la correcta")

else :
  
 print("inCorrecto", nombre,"la alternativa",rpta,"es la respuesta incorrecta")
print("Gracias por responder las preguntas",nombre,",tu puntaje final fue",puntaje,"puntos")



  





