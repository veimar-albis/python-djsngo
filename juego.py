tablero=[" " for i in range(9)] # Creamos el tablero vacío
def imprimir_tablero():
    fila1="| {} | {} | {} |".format(tablero[0],tablero[1],tablero[2])
    fila2="| {} | {} | {} |".format(tablero[3],tablero[4],tablero[5])
    fila3="| {} | {} | {} |".format(tablero[6],tablero[7],tablero[8])
    print("-------------")
    print(fila1)
    print("-------------")
    print(fila2)
    print("-------------")
    print(fila3)
    print("-------------")

imprimir_tablero()
while True:
    
        imprimir_tablero
        movimiento=int(input("Elige una posición del 1 al 9: ").strip())
        if movimiento<1 or movimiento>9:
            print("Movimiento inválido. Intenta de nuevo.")
            continue
        if tablero[movimiento-1]!=" ":
            print("Esa posición ya está ocupada. Intenta de nuevo.")
            continue
        tablero[movimiento-1]="X" # Asignamos la posición elegida por el jugador
        imprimir_tablero()