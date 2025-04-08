#ejercicio1
'''Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.'''
'''divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa = input('Introduce una divisa: ').strip().capitalize()
if divisa in divisas:
    print(f'El símbolo de {divisa} es {divisas[divisa]}')
else:
    print('La divisa no está en el diccionario.')'''
#ejercicio2
'''Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>. '''
'''nombre = input('Introduce tu nombre: ')
edad = input('Introduce tu edad: ')
direccion = input('Introduce tu dirección: ')
telefono = input('Introduce tu teléfono: ')
datos = {'Nombre': nombre, 'Edad': edad, 'Dirección': direccion, 'Teléfono': telefono}
print(f'{nombre} tiene {edad} años, vive en {direccion} y su número de teléfono es {telefono}.')'''
#ejercicio3
'''Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
Fruta 	Precio
Plátano 	1.35
Manzana 	0.80
Pera 	0.85
Naranja 	0.70'''
'''frutas = {'Plátano': 1.35, 'Manzana': 0.80, 'Pera': 0.85, 'Naranja': 0.70}
fruta = input('Introduce una fruta: ').strip().capitalize()
if fruta in frutas:
    kilos = float(input('Introduce el número de kilos: '))
    precio = frutas[fruta] * kilos
    print(f'El precio de {kilos} kilos de {fruta} es {precio}€')
else:
    print('La fruta no está en el diccionario.')'''
#ejercicio4
'''Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.'''
'''fecha = input('Introduce una fecha en formato dd/mm/aaaa: ').lstrip(0)
fecha = fecha.split('/')
dia = fecha[0]  #0  es el dia
mes = fecha[1]  #1 es el mes
anio = fecha[2] #2 es el año
#meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
meses = {
    '1': 'Enero',
    '2': 'Febrero',
    '3': 'Marzo',
    '4': 'Abril',
    '5': 'Mayo',
    '6': 'Junio',
    '7': 'Julio',
    '8': 'Agosto',
    '9': 'Septiembre',
    '10': 'Octubre',
    '11': 'Noviembre',
    '12': 'Diciembre'
}
if mes in meses:
    print(f'{dia} de {meses[mes]} de {anio}')
else:
    print('El mes no es correcto')'''
#ejercicio5
'''Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.'''
asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total_creditos = 0
for asignatura, creditos in asignaturas.items():
    print(f'{asignatura} tiene {creditos} créditos')
    total_creditos += creditos
print(f'El número total de créditos del curso es {total_creditos}')


