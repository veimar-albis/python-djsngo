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
'''def calcular_factura(cantidad, iva=21):
    total = cantidad + (cantidad * iva / 100)
    return total
cantidad = float(input('Introduce la cantidad sin IVA: '))
iva = float(input('Introduce el porcentaje de IVA (por defecto 21): ') or 21)
total = calcular_factura(cantidad, iva)
print(f'El total de la factura es: {total}')'''
#ejercicio5
'''import math
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
print(f'El volumen del cilindro es: {volumen}')'''
#ejercicio6
'''Escribir una función que reciba una muestra de números en una lista y devuelva su media.'''
'''def calcular_media(lista_numeros):
    if len(lista_numeros) == 0:
        return 0
    suma = sum(lista_numeros)
    media = suma / len(lista_numeros)
    return media
numeros = [1, 2, 3, 4, 5]   # Ejemplo de lista de números
media = calcular_media(numeros)
print(f'La media de la lista es: {media}')'''
#ejercicio7
'''Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.'''
'''def calcular_cuadrados(lista_numeros):
    lista_cuadrados = [numero ** 2 for numero in lista_numeros]
    return lista_cuadrados
numeros = [1, 2, 3, 4, 5]   # Ejemplo de lista de números
cuadrados = calcular_cuadrados(numeros)
print(f'Los cuadrados de la lista son: {cuadrados}')'''
#ejercicio8
'''Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.'''
'''def calcular_estadisticas(lista_numeros):
    if len(lista_numeros) == 0:
        return {'media': 0, 'varianza': 0, 'desviacion_tipica': 0}
    media = sum(lista_numeros) / len(lista_numeros)
    varianza = sum((x - media) ** 2 for x in lista_numeros) / len(lista_numeros)
    desviacion_tipica = varianza ** 0.5
    return {'media': media, 'varianza': varianza, 'desviacion_tipica': desviacion_tipica}
numeros = [1, 2, 3, 4, 5]   # Ejemplo de lista de números
estadisticas = calcular_estadisticas(numeros)
print(f'Las estadísticas de la lista son: {estadisticas}')'''
#ejercicio9
'''Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.'''
'''def mcd(a, b):
    while b:
        a, b = b, a % b
    return a
def mcm(a, b):
    return abs(a * b) // mcd(a, b)
a = int(input('Introduce el primer número: '))
b = int(input('Introduce el segundo número: '))
mcd_resultado = mcd(a, b)
mcm_resultado = mcm(a, b)
print(f'El máximo común divisor de {a} y {b} es: {mcd_resultado}')
print(f'El mínimo común múltiplo de {a} y {b} es: {mcm_resultado}')'''
#ejercicio10
'''Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.'''
'''def decimal_a_binario(n):
    if n == 0:
        return '0'
    binario = ''
    while n > 0:
        binario = str(n % 2) + binario
        n //= 2
    return binario
def binario_a_decimal(b):
    decimal = 0
    for i, bit in enumerate(reversed(b)):
        decimal += int(bit) * (2 ** i)
    return decimal
numero_decimal = int(input('Introduce un número decimal: '))
numero_binario = decimal_a_binario(numero_decimal)
print(f'El número decimal {numero_decimal} en binario es: {numero_binario}')
numero_binario = input('Introduce un número binario: ')
numero_decimal = binario_a_decimal(numero_binario)
print(f'El número binario {numero_binario} en decimal es: {numero_decimal}')'''
#ejercicio11
'''Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.'''
def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia
def palabra_mas_repetida(frecuencia):
    max_palabra = max(frecuencia, key=frecuencia.get)
    return (max_palabra, frecuencia[max_palabra])
cadena = input('Introduce una cadena de caracteres: ').lower()
frecuencia = contar_palabras(cadena)
print(f'Frecuencia de palabras: {frecuencia}')
max_palabra, max_frecuencia = palabra_mas_repetida(frecuencia)
print(f'La palabra más repetida es "{max_palabra}" con una frecuencia de {max_frecuencia}.')
