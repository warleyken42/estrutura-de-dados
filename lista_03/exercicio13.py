import os
class Funcionario:
	def __init__(self, nome, salario):
		self.nome = nome
		self.salario = salario

	def mudar_nome(self):
		nome = input("Nome: ")
		self.nome = nome

	def mudar_salario(self):
		salario = input("Salario: ")
		self.salario = salario

	def __repr__(self):
		return "Nome: {}\nSalario: {}".format(self.nome, self.salario)

f = Funcionario("Warley", 0)
os.system("clear")
f.mudar_nome()
f.mudar_salario()
os.system("clear")
print(f)