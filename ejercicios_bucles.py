print(" Ejercicios de bucles")
print("1. Ejercicio 1: Imprimir una palabra 10 veces")
print("2. Ejercicio 2: Imprimir los años cumplidos hasta la edad introducida")
print("3. Ejercicio 3: Imprimir los números impares hasta el número introducido")
print("4. Ejercicio 4: Imprimir los números desde el número introducido hasta 1")
print("5. Ejercicio 5: Calcular el capital acumulado con interés compuesto")
print("6. Ejercicio 6: Imprimir un triángulo de asteriscos")
print("7. Ejercicio 7: Tabla de multiplicar")
print("8. Ejercicio 8: Imprimir números impares en orden inverso")
print("9. Ejercicio 9: Contraseña")
print("10. Ejercicio 10: Verificar si un número es primo")
print("11. Ejercicio 11: Imprimir una palabra al revés")
print("12. Ejercicio 12: Contar letras en una frase")
print("13. Ejercicio 13: Imprimir palabras hasta 'salir'")
print("0. Salir")
opcion = int(input("Selecciona una opción: "))
while opcion!=0:
    print("====================================================================================================")
    if opcion == 0:
        print("Fin del programa")
    elif opcion == 1:
        palabra=input("Introduce una palabra: ")
        for i in range(1,11):
            print(palabra)
    elif opcion == 2:
        edad=int(input("Introduce tu edad: "))
        for i in range(1,edad)+1:
            print("cumpliste",i,"años")
    elif opcion == 3:
        numero=int(input("Introduce un número: "))
        for i in range(1,numero):
            if i%2!=0:
                print(i,end=",")
    elif opcion == 4:
        numero=int(input("Introduce un número: "))
        for i in range(numero,0,-1):
            print(i,end=",")
    elif opcion == 5:
        capital=float(input("Introduce el capital a invertir: "))
        interes=float(input("Introduce el interes: "))
        tiempo=int(input("Introduce el tiempo: "))
        for i in range(1,tiempo+1):
            capital=capital+(capital*interes/100)
            print("El capital al año",i,"es de",capital)
    elif opcion == 6:
        altura=int(input("Introduce la altura del triángulo: "))
        for i in range(1,altura+1):
            for j in range(1,i+1):
                print("*",end="")
            print()
    elif opcion == 7:
        for i in range(1,11):
            for j in range(1,11):
                print(i,"*",j,"=",i*j,end="\t")
            print()
    elif opcion == 8:
        numero=int(input("Introduce un número: "))
        for i in range(1,numero,2):
            for j in range(i,0,-1):
                if j%2!=0:
                    print(j,end="")
            print()
    elif opcion == 9:
        contraseña=input("Introduce la contraseña: ")
        confirmacion=input("Confirma la contraseña: ")
        while confirmacion!=contraseña:
            print("Contraseña incorrecta")
            confirmacion=input("Introduce la contraseña:")
        print("Contraseña correcta")
    elif opcion == 10:
        supuesto_primo=int(input("Introduce un número: "))
        for i in range(2,supuesto_primo):
            if supuesto_primo%i==0:
                print("No es primo")
                break
        else:
            print("Es primo")
    elif opcion == 11:
        palabra=input("Introduce una palabra: ")
        for i in palabra [::-1]:
            print(i,end=" ")
        print()
    elif opcion == 12:
        frase=input("Introduce una frase: ")
        letra_busqueda=input("Introduce una letra: ")
        contador=0
        for i in (frase):
            if i==letra_busqueda:
                contador+=1
        print("La letra",letra_busqueda,"se repite",contador,"veces")
    elif opcion == 13:
        palabra=input("Introduce una palabra: ")
        while palabra!="salir":
            print(palabra)
            palabra=input("Introduce una palabra: ")
        print("Fin del programa")
    else:
        print("Opción no válida")
    print("                Ejercicios de bucles")
    print("                ====================")    
    print("1. Ejercicio 1: Imprimir una palabra 10 veces")
    print("2. Ejercicio 2: Imprimir los años cumplidos hasta la edad introducida")
    print("3. Ejercicio 3: Imprimir los números impares hasta el número introducido")
    print("4. Ejercicio 4: Imprimir los números desde el número introducido hasta 1")
    print("5. Ejercicio 5: Calcular el capital acumulado con interés compuesto")
    print("6. Ejercicio 6: Imprimir un triángulo de asteriscos")
    print("7. Ejercicio 7: Tabla de multiplicar")
    print("8. Ejercicio 8: Imprimir números impares en orden inverso")
    print("9. Ejercicio 9: Contraseña")
    print("10. Ejercicio 10: Verificar si un número es primo")
    print("11. Ejercicio 11: Imprimir una palabra al revés")
    print("12. Ejercicio 12: Contar letras en una frase")
    print("13. Ejercicio 13: Imprimir palabras hasta 'salir'")
    print("0. Salir")
    opcion = int(input("Selecciona una opción: "))
    #Ejercicios de bucles







#Ejercicio1
''''''
#ejercicio2
'''edad=int(input("Introduce tu edad: "))
for i in range(1,edad):
    print("cumpliste",i,"años")'''
#ejercicio3
'''numero=int(input("Introduce un número: "))
for i in range(1,numero):
    if i%2!=0:
        print(i,end=",")'''
#ejercicio4
'''numero=int(input("Introduce un número: "))
for i in range(numero,0,-1):
    print(i,end=",")'''
#ejercicio5
'''capital=float(input("Introduce el capital a invertir: "))
interes=float(input("Introduce el interes: "))
tiempo=int(input("Introduce el tiempo: "))
for i in range(1,tiempo+1):
    capital=capital+(capital*interes/100)
    print("El capital al año",i,"es de",capital)'''
#ejercicio6
'''altura=int(input("Introduce la altura del triángulo: "))
for i in range(1,altura+1):
    for j in range(1,i+1):
        print("*",end="")
    print()'''
#ejercicio7
'''for i in range(1,11):
    for j in range(1,11):
        print(i,"*",j,"=",i*j,end="\t")
    print()'''
#ejercicio8
'''numero=int(input("Introduce un número: "))
for i in range(1,numero,2):
    for j in range(i,0,-1):
        if j%2!=0:
            print(j,end="")
    print()'''
#ejercicio9
'''contraseña=input("Introduce la contraseña: ")
confirmacion=input("Confirma la contraseña: ")
while confirmacion!=contraseña:
    print("Contraseña incorrecta")
    confirmacion=input("Introduce la contraseña:")
print("Contraseña correcta")'''
#ejercicio10
'''supuesto_primo=int(input("Introduce un número: "))
for i in range(2,supuesto_primo):
    if supuesto_primo%i==0:
        print("No es primo")
        break
else:
    print("Es primo")'''
#ejercicio11
'''palabra=input("Introduce una palabra: ")
for i in palabra [::-1]:
    print(i,end=" ")
print()'''
#ejercicio12
'''frase=input("Introduce una frase: ")
letra_busqueda=input("Introduce una letra: ")
contador=0
for i in (frase):
    if i==letra_busqueda:
        contador+=1
print("La letra",letra_busqueda,"se repite",contador,"veces")'''
#ejercicio13
'''palabra=input("Introduce una palabra: ")
while palabra!="salir":
    print(palabra)
    palabra=input("Introduce una palabra: ")
print("Fin del programa")'''
