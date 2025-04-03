import math
#ejer 1
print("hola mundo")

#ejer2
#n=input("cual es tu nombre?: ")
#print("hola "+n)

#ej 3
a=pow((3+2)/(2*5),2)
print(a)

#ejer4
"""a=input("cuantas horas trabajaste?: ")
b=input("cuanto te pagan por hora?: ")
print(type(a))
s=int(a)*int(b)
print("deben pagarte " + str(s))"""

#ejer5
"""n=int(input("ingrese valor de n: "))
r=int((n*(n+1))/2)
print("la suma de enteros es " + str(r) )"""

#ejer6
"""peso=float(input("ingrese opeso en kg: "))
estatura=float(input("ingrese estatira en metros: "))
IMC=peso/estatura**2
print("su IMC es "+str(IMC))"""  

#ejer7
'''n1=int(input("Ingrese el dividendo: "))
n2=int(input("ingrese el divisor: "))
print("el cociente de la division es: "+str(n1//n2))
print("el resido de la division es: "+str(n1%n2))'''

#ejer9
'''cap=float(input("ingrese elmonto a invertir: "))
i=float(input("ingrese el interes anual: "))
time=int(input("ingrese el numero de años: "))
gan=cap*(i/100)+1*time
print("el interes ganado es "+str(gan))'''

#ejer10
'''p=int(input("ingrese la cantidad de payasos: "))
m=int(input("ingrese la cantidad de muñecas: "))
peso=p*112+m*75
print("wl peso para calcular el precio es: "+str(peso))'''

#ejer12
prec=3.49
desc=0.6
pan=int(input("inrese la cantidad de panes guardados: "))
print("el precio normal de pan fresco es de "+str(prec)+" por barra")
print("el descuento por no ser fresco es de: "+str(prec*desc)+" por barra")
print("el precio total de su compra es: "+str(pan*prec*desc))