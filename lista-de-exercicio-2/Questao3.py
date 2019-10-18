sexo =  input("Informe o sexo (F) Feminino e (M) Masculino: ")
sexo = sexo.upper()
print(sexo)
if sexo == 'F':
	print("Feminino")
elif sexo == 'M':
	print("Masculino")
else:
	print("Sexo invalido")