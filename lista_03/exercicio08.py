class Macaco:

    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, objeto):
        self.bucho.append(objeto)

    def verBucho(self):
        print("Coisas no Bucho: ")
        for i in self.bucho:
            print(i)
        print("...")

    def digerir(self):
        print("Digerindo...")
        print("\n")
        self.verBucho()
        self.bucho = []

    def imprimir(self):
    	print("Nome: {}".format(self.nome))

m1 = Macaco("João")
m1.imprimir()
m1.comer("Banana")
m1.verBucho()
m1.digerir()

m2 = Macaco("Jardel")
m2.imprimir()
m2.comer("Maca")
m2.verBucho()
m2.digerir()

m1 = Macaco("João")
m1.imprimir()
m1.comer("Manga")
m1.verBucho()
m1.digerir()

m2 = Macaco("Jardel")
m2.imprimir()
m2.comer("Melão")
m2.verBucho()
m2.digerir()
