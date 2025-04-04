class Libra:
    valor = 1.00
    color="dorado"
    num_bordes=1
    diametro=22.5 # mm
    espesor=3.15 # mm
    caras=True
moneda1=Libra()
print(type(moneda1))
print(moneda1.valor)
print(moneda1.color)
moneda1.color="plateado"
print(moneda1.color)
