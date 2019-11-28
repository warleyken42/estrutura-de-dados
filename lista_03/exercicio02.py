class Quadrado:
    def __init__(self, lado):
        self.lado = lado
    def troca_lado(self, lado):
        self.lado = lado
    def mostra_lado(self):
        print("Meu lado é {}".format(self.lado))
    def perimetro(self):
        return 4 * self.lado
    def area(self):
        return self.lado ** 2

quadrado1 = Quadrado(2)
quadrado1.mostra_lado()
quadrado1.troca_lado(3)
quadrado1.mostra_lado()
quadrado1.mostra_lado()
print("Perimetro: {} \nArea: {}".format(quadrado1.perimetro(), quadrado1.area()))