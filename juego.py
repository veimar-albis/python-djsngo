#programa juego tic tac toe
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
imprimir_tablero() # Imprimimos el tablero vacío
def jugar(jugador):
    posicion=int(input("Jugador {}, elige una posición (1-9): ".format(jugador)))
    if tablero[posicion-1]==" ":
        tablero[posicion-1]=jugador
        imprimir_tablero()
    else:
        print("Esa posición ya está ocupada. Elige otra.")
        jugar(jugador)
def verificar_ganador():
    combinaciones_ganadoras=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for combinacion in combinaciones_ganadoras:
        if tablero[combinacion[0]]==tablero[combinacion[1]]==tablero[combinacion[2]]!=" ":
            return True
    return False
def verificar_empate():
    for i in tablero:
        if i==" ":
            return False
    return True
# Programa principal
jugador_actual="X"
while True:
    jugar(jugador_actual)
    if verificar_ganador():
        print("¡Jugador {} gana!".format(jugador_actual))
        break
    if verificar_empate():
        print("¡Es un empate!")
        break
    jugador_actual="O" if jugador_actual=="X" else "X"
    # Cambiamos de jugador
    
