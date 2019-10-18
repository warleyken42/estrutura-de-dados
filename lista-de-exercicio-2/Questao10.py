horario =  input("Qual o turno que estuda (M) Matutino, (V) Vespertino ou (N) Noturno: ")
horario = horario.upper()

if horario == 'M':
	print("Bom dia!")
elif horario == 'V':
	print("Boa tarde!")
else:
	print("Boa noite!")