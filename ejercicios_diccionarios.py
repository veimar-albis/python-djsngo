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
'''asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total_creditos = 0
for asignatura, creditos in asignaturas.items():
    print(f'{asignatura} tiene {creditos} créditos')
    total_creditos += creditos
print(f'El número total de créditos del curso es {total_creditos}')'''
#ejercicio6
'''Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.'''
'''persona = {}
while True:
    clave = input('Qué dato desea guardar? ( ingrese datos de la persona en el formato {calve:valor}, ó "salir" para terminar): ')
    if clave.lower() == 'salir':
        break
    valor = input(f'Introduce el valor para {clave}: ')
    persona[clave] = valor
    print(persona)'''
#ejercicio7
'''Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato
Lista de la compra 	
Artículo 1 	Precio
Artículo 2 	Precio
Artículo 3 	Precio
… 	…
Total 	Coste'''
'''cesta = {}
while True:
    articulo = input('Introduce el nombre del artículo y su costo (o "salir" para terminar): ')
    if articulo.lower() == 'salir':
        break
    precio = float(input(f'Introduce el precio de {articulo}: '))
    cesta[articulo] = precio
print('Lista de la compra')
print('Artículo\tPrecio')
total = 0
for articulo, precio in cesta.items():
    print(f'{articulo}\t{precio}')
    total += precio
print(f'Total: {total}')'''
#ejercicio8
'''Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.'''
traduccion = input('Introduce las palabras en español e inglés separadas por dos puntos y cada par separado por comas: ')
traduccion = traduccion.split(',')
diccionario = {}
for par in traduccion:
    palabra, traduccion = par.split(':')
    diccionario[palabra.strip()] = traduccion.strip()
frase = input('Introduce una frase en español: ')
frase = frase.split()
traduccion_frase = []
for palabra in frase:
    if palabra in diccionario:
        traduccion_frase.append(diccionario[palabra])
    else:
        traduccion_frase.append(palabra)
print(' '.join(traduccion_frase))