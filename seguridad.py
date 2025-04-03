usuarios_conocidos=["Alice","Bob","Claire","Dan","Emma","Fred","Georgie","Harry"]

while True:
    print("Hola mi nombre es Keto")
    nombre=input("Cual es tu no mbre?: ").strip().capitalize()
    if nombre in usuarios_conocidos:
        print("Hola {}!".format(nombre))
        eliminar=input("te gustaria ser eliminado de la lista? y/n: ").lower()
        if eliminar=="y":
            print(usuarios_conocidos)
            usuarios_conocidos.remove(nombre)
            print(usuarios_conocidos)
    else:
        agregar=input("No logro reconocerte {} , te gustaria ser agregado a la lista? y/n:".format(nombre)).lower()
        if agregar=="y":
            print(usuarios_conocidos)
            usuarios_conocidos.append(nombre) 
            print(usuarios_conocidos)