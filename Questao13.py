sexo = int(input("Informe seu sexo: (1)Para Homem (2)Para mulher: "))

if sexo == 1:
  print("Homem")
  altura = float(input("Digite sua altura = "))
  valor = 72.7 * altura
  retorna = valor - 58
  print("Seu peso ideal = {:.2f}".format(retorna), "Kg")
elif sexo == 2:
  print("Mulher")
  altura = float(input("Digite sua altura = "))
  valor = 62.1 * altura
  retorna = valor - 44.7
  print("Seu peso ideal = {:.2f}".format(retorna), "Kg")
