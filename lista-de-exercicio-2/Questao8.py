produto1 = input("Informe o preço do produto 1: ")
produto2 = input("Informe o preço do produto 2: ")
produto3 = input("Informe o preço do produto 3: ")

if produto1 < produto2 and produto3:
	print("O produto 1 é o mais barato!")
elif produto2 < produto1 and produto3:
	print("O produto 2 é o mais barato")
elif produto3 < produto1 and produto2:
	print("O produto 3 é o mais barato")
else:
    print("Todos os preços são iguais!!")

