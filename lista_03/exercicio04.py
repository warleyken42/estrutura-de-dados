class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        if self.idade < 21:
            self.altura += 0.5

        self.idade += 1

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura


    def mostraPessoa(self):
        print("Nome: {}, idade: {} anos, peso: {}kg, altura: {}cm".format(self.nome, self.idade, self.peso, self.altura))


war = Pessoa('Warley', 17, 54, 163)
war.mostraPessoa()
war.envelhecer()
war.mostraPessoa()
war.envelhecer()
war.mostraPessoa()
war.envelhecer()
war.mostraPessoa()
war.envelhecer()
war.mostraPessoa()
war.envelhecer()
war.emagrecer(3)
war.mostraPessoa()