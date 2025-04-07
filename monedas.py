import random
class Libra:
#constructor de la clase Libra
    def __init__(self, raro=False):
        self.raro = raro
        if self.raro:
            self.valor = 1.25
        else:
            self.valor = 1.0

        self.color = "dorado"
        self.num_bordes = 1
        self.diametro = 22.5
        self.espesor = 3.15
        self.caras = True
#Destructor de la clase Libra
    def __del__(self):
        print("Moneda gastada")
#define metodos para cambiar el color de la moneda
    def oxido(self):
        self.color = "verde"

    def limpiar(self):
        self.color = "dorado"

    def vueltas(self):
        caras_opciones[True,False]
        eleccion = random.choice(caras_opciones)
        self.caras = eleccion
        return self.caras



moneda1 = Libra()

print(moneda1.color)
moneda1.oxido()
print(moneda1.color)
moneda1.limpiar()
print(moneda1.color)
del moneda1
