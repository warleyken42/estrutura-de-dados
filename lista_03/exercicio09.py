class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "Ponto({}, {})".format(self.x, self.y)

class Retangulo:
    def __init__(self, canto1, canto2):
        self.canto1 = canto1
        self.canto2 = canto2
    def centro(self):
        x_centro = (self.canto1.x + self.canto2.x) / 2.0
        y_centro = (self.canto1.y + self.canto2.y) / 2.0
        return Ponto(x_centro, y_centro)

x1 = input("Valor de X no canto inferior esquerdo: ")
y1 = input("Valor de Y do canto inferior esquerdo: ")
canto1 = Ponto(x1, y1)
x2 = input("Valor de X do canto superior direito: ")
y2 = input("Valor de Y do canto superior direito: ")
canto2 = Ponto(x2, y2)
ret = Retangulo(canto1, canto2)
print("Ponto central: {}".format(ret.centro()))