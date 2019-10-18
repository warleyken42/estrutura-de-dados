salario = float(input("Digite seu salario: "))

if salario <= 280:
  porcetagem = (20 / 100.0) * salario
  total = salario + porcetagem

  print("Seu salario antes do reajuste = R${}".format(salario))
  print("O percentual de aumento 20 %")
  print("O valor do aumento = R${}".format(porcetagem))
  print("Com o reajuste, novo salario = R${}".format(total))

elif salario > 280 and salario <= 700:
  porcetagem = (15 / 100.0) * salario
  total = salario + porcetagem
  print("Seu salario antes do reajuste = R${}".format(salario))
  print("O percentual de aumento 15 %")
  print("O valor do aumento = R${}".format(porcetagem))
  print("Com o reajuste, novo salario = R${}".format(total))

elif salario > 700 and salario <= 1500:
  porcetagem = (10 / 100.0) * salario
  total = salario + porcetagem
  print("Seu salario antes do reajuste = R${}".format(salario))
  print("O percentual de aumento 10 %")
  print("O valor do aumento = R${}".format(porcetagem))
  print("Com o reajuste, novo salario = R${}".format(total))

elif salario > 1500:
  porcetagem = (5 / 100.0) * salario
  total = salario + porcetagem
  print("Seu salario antes do reajuste = R${}".format(salario))
  print("O percentual de aumento 5 %")
  print("O valor do aumento = R${}".format(porcetagem))
  print("Com o reajuste, novo salario = R${}".format(total))