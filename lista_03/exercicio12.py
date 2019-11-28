class ContaInvestimento:
    def __init__(self, nome, saldo, taxa_juros = 10):
        self.correntista = nome
        self.saldo = saldo
        self.taxa_juros = taxa_juros

    def alterar_nome(self, nome):
        self.correntista = nome

    def deposito(self, valor):
        self.saldo = self.saldo + valor

    def saque(self, valor):
        self.saldo = self.saldo - valor

    def adicionar_juros(self):
        self.taxa_juros = (self.saldo*0.10)
        self.saldo = self.taxa_juros + self.saldo

    def imprimir(self):
        print("Nome do correntista: {}\nSaldo da conta: {}".format(self.correntista, self.saldo))

    def imprimir_com_juros(self):
        print("Nome do correntista: {}\nNovo Saldo: {}\nDinheiro do Juros de 10%: {}".format(self.correntista, self.saldo, self.taxa_juros))

conta1 = ContaInvestimento("Warley Kennedy", 1000)
conta1.imprimir()
print("\n")
conta1.adicionar_juros()
conta1.imprimir_com_juros()
print("\n")
conta1.adicionar_juros()
conta1.imprimir_com_juros()
print("\n")
conta1.adicionar_juros()
conta1.imprimir_com_juros()
print("\n")
conta1.adicionar_juros()
conta1.imprimir_com_juros()
print("\n")
conta1.adicionar_juros()
conta1.imprimir_com_juros()
print("\n")

