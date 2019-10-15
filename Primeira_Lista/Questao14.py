peso = int(input("Entre com o peso: "))
if peso > 50:
	excesso = peso - 50
	multa   = excesso * 4.00
else:
	excesso = "ZERO"
	multa = "ZERO"
  
print("O excesso de peso =",str(excesso),"kg e a multa = R$", str(multa))