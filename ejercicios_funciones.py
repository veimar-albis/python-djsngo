#ejercicio1
'''def saludo():
    print('¡Hola amiga!')
n=int(input('Cuantas veces quieres que se muestre el saludo? '))
for i in range(n):
    saludo()'''
#ejercicio2
'''def saludo(nombre):
    print(f'¡Hola {nombre}!')
nombre = input('Introduce tu nombre: ')
saludo(nombre)'''
#ejercicio3
'''def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
n = int(input('Introduce un número entero positivo: '))
resultado = factorial(n)
print(f'El factorial de {n} es {resultado}')'''
#ejercicio4
def calcular_factura(cantidad, iva=21):
    total = cantidad + (cantidad * iva / 100)
    return total
cantidad = float(input('Introduce la cantidad sin IVA: '))
iva = float(input('Introduce el porcentaje de IVA (por defecto 21): ') or 21)
total = calcular_factura(cantidad, iva)
print(f'El total de la factura es: {total}')
#ejercicio5
"Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función."
import math
def area_circulo(radio):
    return math.pi * radio ** 2
def volumen_cilindro(radio, altura):
    area = area_circulo(radio)
    return area * altura
radio = float(input('Introduce el radio del cilindro: '))
altura = float(input('Introduce la altura del cilindro: '))
area = area_circulo(radio)
volumen = volumen_cilindro(radio, altura)
print(f'El área del círculo es: {area}')
print(f'El volumen del cilindro es: {volumen}')
