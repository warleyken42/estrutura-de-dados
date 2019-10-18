lado1 = int(input("Digite o tamanho do primeiro lado: "))
lado2 = int(input("Digite o tamanho do segundo lado: "))
lado3 = int(input("Digite o tamanho do segundo lado: "))

if lado1 + lado2 > lado3:
	if lado1 == lado2 and lado1 == lado3:
		print("Triângulo Equilátero")
	elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
		print("Triângulo Isósceles")
	elif lado1 != lado2 and lado3 or lado2 != lado1 and lado3 or lado1 != lado3:
		print("Triângulo Escaleno")
else:
    print("É impossivel ser um triângulo")