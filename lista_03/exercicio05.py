class Conta:
    def __init__(self, nome, numero, saldo = 0):
        self.correntista = nome
        self.numero = numero
        self.saldo = saldo
    def alterar_nome(self, nome):
        self.correntista = nome
    def deposito(self, valor):
        self.saldo = self.saldo + valor
    def saque(self, valor):
        self.saldo = self.saldo - valor
    def imprimir(self):
        print("Nome do correntista: {}\nNumero da conta: {}\nSaldo da conta: {}".format(self.correntista, self.numero, self.saldo))

conta1 = Conta("Warley Kennedy", 10759.4)
conta1.imprimir()
print("\n")
conta1.alterar_nome("Lucas Caua")
conta1.imprimir()
print("\n")
conta1.deposito(1000)
conta1.imprimir()
print("\n")
conta1.saque(500)
conta1.imprimir()
