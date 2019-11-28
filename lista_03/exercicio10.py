class Bomba:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_litro):
        self.quantidade_litro = quantidade_litro
        self.valor_litro = valor_litro
        self.tipo_combustivel = tipo_combustivel
    
    def abastecer_valor(self, valor):
        litros = valor / self.valor_litro
        self.quantidade_litro = self.quantidade_litro - litros
        return litros
    
    def abastecer_litro(self, litros):
        valor = litros * self.valor_litro
        self.quantidade_litro = self.quantidade_litro - litros
        return valor
    
    def alterar_valor(self, valor_litro):
        self.valor_litro = valor_litro
    
    def alterar_combustivel(self, tipo_combustivel):
        self.tipo_combustivel = tipo_combustivel
    
    def __repr__(self):
      return "Tipo do Combustivel : {}\nPreço do Combustivel: {}\nQuantidade de Litros: {}".format(self.tipo_combustivel, self.valor_litro, self.quantidade_litro)
    
    
bomba = Bomba("Gasolina", 4.00, 100)
print(bomba)
print("\n")
bomba.alterar_combustivel("Diesel")
print(bomba)
print("\n")
bomba.alterar_valor(5.00)
print(bomba)