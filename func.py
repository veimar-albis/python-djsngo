'''def agregar(*numeros):
    total=0
    for numero in numeros:
        total+=numero
    return total

print(agregar(1,2,3,4,5))'''

'''def sobre (nombre,edad,gustos):
    oracion="Es {} tiene {} años y le gusta {}".format(nombre,edad,gustos)
    return oracion

dictionary={"nombre":"Jack","edad":20,"gustos":"python"}
print(sobre(**dictionary))'''



def mi_funcion(**kwargs):
     for key, value in kwargs.items():
        print(f"{key}: {value}")