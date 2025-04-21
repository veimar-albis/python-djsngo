#ejercicio1
'''divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa = input('Introduce una divisa: ').strip().capitalize()
if divisa in divisas:
    print(f'El símbolo de {divisa} es {divisas[divisa]}')
else:
    print('La divisa no está en el diccionario.')'''
#ejercicio2
'''nombre = input('Introduce tu nombre: ')
edad = input('Introduce tu edad: ')
direccion = input('Introduce tu dirección: ')
telefono = input('Introduce tu teléfono: ')
datos = {'Nombre': nombre, 'Edad': edad, 'Dirección': direccion, 'Teléfono': telefono}
print(f'{nombre} tiene {edad} años, vive en {direccion} y su número de teléfono es {telefono}.')'''
#ejercicio3
'''frutas = {'Plátano': 1.35, 'Manzana': 0.80, 'Pera': 0.85, 'Naranja': 0.70}
fruta = input('Introduce una fruta: ').strip().capitalize()
if fruta in frutas:
    kilos = float(input('Introduce el número de kilos: '))
    precio = frutas[fruta] * kilos
    print(f'El precio de {kilos} kilos de {fruta} es {precio}€')
else:
    print('La fruta no está en el diccionario.')'''
#ejercicio4
'''fecha = input('Introduce una fecha en formato dd/mm/aaaa: ')
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
'''asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total_creditos = 0
for asignatura, creditos in asignaturas.items():
    print(f'{asignatura} tiene {creditos} créditos')
    total_creditos += creditos
print(f'El número total de créditos del curso es {total_creditos}')'''
#ejercicio6
'''persona = {}
while True:
    clave = input('Qué dato desea guardar? ( ingrese datos de la persona en el formato {calve:valor}, ó "salir" para terminar): ')
    if clave.lower() == 'salir':
        break
    valor = input(f'Introduce el valor para {clave}: ')
    persona[clave] = valor
    print(persona)'''
#ejercicio7
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
traduccion = input('Introduce las palabras en español e inglés separadas por dos puntos y cada par separado por comas: ')# ejemplo: 'casa:house, perro:dog, gato:cat'
traduccion = traduccion.split(',')# separa los pares por comas
diccionario = {}
for par in traduccion:# separa cada par por dos puntos
    palabra, traduccion = par.split(':')
    diccionario[palabra.strip()] = traduccion.strip()# añade al diccionario
frase = input('Introduce una frase en español: ')
frase = frase.split()
traduccion_frase = []
for palabra in frase:# traduce cada palabra de la frase
    if palabra in diccionario:# si la palabra está en el diccionario
        traduccion_frase.append(diccionario[palabra])# añade la traducción
    else:# si la palabra no está en el diccionario
        traduccion_frase.append(palabra)# añade la palabra sin traducir
print(' '.join(traduccion_frase))
#ejercicio9
'''facturas = {}
total_cobrado = 0
total_pendiente = 0
while True:
    opcion = input('¿Quieres añadir una nueva factura, pagar una existente o terminar? (añadir/pagar/terminar): ')
    if opcion.lower() == 'añadir':# añadir una nueva factura
        num_factura = input('Introduce el número de factura: ')
        coste = float(input('Introduce el coste de la factura: '))
        facturas[num_factura] = coste
        total_pendiente += coste
    elif opcion.lower() == 'pagar':# pagar una factura existente
        num_factura = input('Introduce el número de factura a pagar: ')
        if num_factura in facturas:# si la factura existe
            total_cobrado += facturas[num_factura]
            total_pendiente -= facturas[num_factura]
            del facturas[num_factura]
        else:# si la factura no existe
            print('La factura no existe.')
    elif opcion.lower() == 'terminar':# terminar el programa
        break
    else:
        print('Opción no válida.')
    print(f'Total cobrado: {total_cobrado}')
    print(f'Total pendiente de cobro: {total_pendiente}')'''

