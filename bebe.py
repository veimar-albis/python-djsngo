from random import choice
preguntas=["Por que el cielo es azul?: ","Porque hay una cara en la luna?: ","Donde estan los dinosaurios?: ","por que hay gente pobre?: "]
pregunta=choice(preguntas)
respuesta=input(pregunta.lower().strip())
while respuesta!="porque si":
    respuesta=input("Por que?: ").lower().strip()
print("aaaahhhh, bueno")