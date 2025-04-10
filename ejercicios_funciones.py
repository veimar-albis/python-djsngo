#ejercicio1
'''Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.'''
'''def saludo():
    print('¡Hola amiga!')
n=int(input('Cuantas veces quieres que se muestre el saludo? '))
for i in range(n):
    saludo()'''
#ejercicio2
'''Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.'''
'''def saludo(nombre):
    print(f'¡Hola {nombre}!')
nombre = input('Introduce tu nombre: ')
saludo(nombre)'''
#ejercicio3
'''Escribir una función que reciba un número entero positivo y devuelva su factorial.'''
'''def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
n = int(input('Introduce un número entero positivo: '))
resultado = factorial(n)
print(f'El factorial de {n} es {resultado}')'''
#ejercicio4
'''Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.'''
def calcular_factura(cantidad, iva=21):
    total = cantidad + (cantidad * iva / 100)
    return total
cantidad = float(input('Introduce la cantidad sin IVA: '))
iva = float(input('Introduce el porcentaje de IVA (por defecto 21): ') or 21)
total = calcular_factura(cantidad, iva)
print(f'El total de la factura es: {total}')
#ejercicio5