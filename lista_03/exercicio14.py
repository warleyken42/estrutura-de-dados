import os
class Funcionario:
	def __init__(self, nome, salario, taxa_juros = 10):
		self.nome = nome
		self.salario = salario
		self.taxa_juros = taxa_juros

	def mudar_nome(self):
		nome = input("Nome: ")
		self.nome = nome

	def mudar_salario(self):
		salario = input("Salario: ")
		self.salario = salario

	def percentual(self):
    self.taxa_juros = (self.salario*0.10)
    self.salario = self.taxa_juros + self.salario

	def imprimir(self):
    print("Nome: {}\nSalario: {}".format(self.nome, self.salario))

  def imprimir_com_juros(self):
    print("Nome: {}\nSalario: {}\nDinheiro do Juros de 10%: {}".format(self.nome, self.salario, self.taxa_juros))


f = Funcionario("Warley", 0)
os.system("clear")
f.mudar_nome()
f.mudar_salario()
f.imprimir()
os.system("clear")
print(f)