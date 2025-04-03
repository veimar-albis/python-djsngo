peliculas={
    "Nemo":[3,5],
    "Bourne":[18,5],
    "Tarzan":[15,5],
    "Spiderman":[15,5]
}

while True:
    eleccion=input("Que pelicula te gustaria ver?: ").strip().title()
    if eleccion in peliculas:
        edad=int(input("Cuantos anios tienes?: ").strip())
        if edad>=peliculas[eleccion][0]:
            if peliculas[eleccion][1]>0:
                print("Disfruta la pelicula")
                peliculas[eleccion][1]=peliculas[eleccion][1]-1
            else:
                print("lo siento, no quedan boletos para esa pelicula")    
        else:
            print("eres muy joven para ver esa pelicula")
    else:
        print("No tenemos esa pelicula")