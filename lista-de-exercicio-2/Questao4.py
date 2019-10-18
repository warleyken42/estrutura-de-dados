letra = input("Digite uma letra: ")
letra = letra.upper()

if letra not in ['a', 'e', 'i', 'o', 'u']:
	print("A letra é uma vogal")
else:
	print("A letra é uma consoante!")