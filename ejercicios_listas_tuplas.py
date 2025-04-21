# Ejercicio 1
'''cantidad=int(input("Ingrese la cantidad de materias a registrar: "))
materia = []
for i in range(cantidad):
    materia.append(input("Ingrese el nombre de la materia: "))
print("La lista de materias es: ", materia)'''
# Ejercicio 2
'''cantidad=int(input("Ingrese la cantidad de materias a registrar: "))
materias = []
for i in range(cantidad):
    materias.append(input("Ingrese el nombre de la materia: "))
for materia in materias:
    print("yo estudio: ",materia)'''
# Ejercicio 3
'''Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.'''
'''materiaa=[]
n=int(input("Ingrese la cantidad de materias a registrar: "))
for i in range(n):
    materiaa.append(input("Ingrese el nombre de la materia: "))
for i in range(n):
    nota=int(input("Ingrese la nota de la materia: "))
    print(f"En {materiaa[i]} has sacado {nota}")'''
# Ejercicio 4
'''Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.'''
'''numeros_ganadores = []
cantidad = int(input("Ingrese la cantidad de numeros ganadores: "))
for i in range(cantidad):
    numero = int(input("Ingrese el numero ganador: "))
    numeros_ganadores.append(numero)
numeros_ganadores.sort()
print("Los numeros ganadores son: ", numeros_ganadores)'''
# Ejercicio 5
'''Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.'''
'''numeros = list(range(1, 11))
numeros.reverse()
print("Los numeros del 1 al 10 en orden inverso son: ", end="")
for i in range(len(numeros)-1):
    print(numeros[i], end=", ")
print(numeros[-1])'''
# Ejercicio 6
'''materiaa=[]
n=int(input("Ingrese la cantidad de materias a registrar: "))
for i in range(n):
    materiaa.append(input("Ingrese el nombre de la materia: "))

for materia in range(n):
    print("Ingrese la nota de la materia ", materiaa[materia],": ")
    nota=int(input())
    if nota > 50:
        materiaa.remove(materiaa[materia])
        n-=1
        materia-=1'''
# Ejercicio 7
'''abecedario = list("abcdefghijklmnopqrstuvwxyz")
print("El abecedario original es: ", end="")
for i in range(len(abecedario)-1):
    print(abecedario[i], end=", ")
print("")
abecedario = [letra for i, letra in enumerate(abecedario) if (i + 1) % 3 != 0]
print("El abecedario sin letras en posiciones múltiplos de 3 es: ", end="")
for i in range(len(abecedario)-1):
    print(abecedario[i], end=", ")
print(abecedario[-1])'''
# Ejercicio 8
'''palabra = input("Ingrese una palabra: ")
palabra = palabra.lower()
palabra = palabra.replace(" ", "")
palabra = list(palabra)
palabra_invertida = palabra[::-1]
if palabra == palabra_invertida:
    print("La palabra es un palíndromo")
else:
    print("La palabra no es un palíndromo")'''
# Ejercicio 9
'''palabra = input("Ingrese una palabra: ")
vocales = ['a', 'e', 'i', 'o', 'u']
contador_vocales = {vocal: 0 for vocal in vocales}
for letra in palabra.lower():
    if letra in vocales:
        contador_vocales[letra] += 1
for vocal, contador in contador_vocales.items():
    print(f"La vocal {vocal} aparece {contador} veces")'''
# Ejercicio 10
'''precios = [50, 75, 46, 22, 80,100, 65, 8]
menor = min(precios)
mayor = max(precios)
print(f"El menor precio es: {menor}")
print(f"El mayor precio es: {mayor}")'''
# Ejercicio 11
'''vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
producto_escalar = sum(a * b for a, b in zip(vector1, vector2))
print(f"El producto escalar de los vectores es: {producto_escalar}")'''
# Ejercicio 12

'''matriz1 = [[1, 2, 3], [4, 5, 6]]
matriz2 = [[-1,0], [0,1], [1,1]]
producto = [[0, 0], [0, 0]]
for i in range(len(matriz1)):# recorre las filas de la matriz 1
    for j in range(len(matriz2[0])):# recorre las columnas de la matriz 2
        for k in range(len(matriz2)):# recorre las filas de la matriz 2
            producto[i][j] += matriz1[i][k] * matriz2[k][j]#mulplica la fila de la matriz 1 por la columna de la matriz 2
print("El producto de las matrices es:")
for fila in producto:
    print(fila)'''
# Ejercicio 13
numeros = input("Ingrese una muestra de numeros separados por comas: ")# pide al usuario que ingrese los numeros separados por comas
numeros = numeros.split(",")# separa los numeros por comas y los guarda en una lista
numeros = [float(numero) for numero in numeros] #convierte la lista de string a float
#calcula la media y desviacion tipica
media = sum(numeros) / len(numeros)
desviacion = (sum((x - media) ** 2 for x in numeros) / len(numeros)) ** 0.5
print(f"La media es: {media}")
print(f"La desviacion tipica es: {desviacion}")