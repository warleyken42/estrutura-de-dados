quantidade_hora = float(input("Quanto você ganha por hora: "))
hora_trabalho = float(input("Quantas horas você trabalhou: "))

salario_bruto = quantidade_hora * hora_trabalho

ir = (11/100.0 * salario_bruto)
inss = (8/100.0 * salario_bruto)
sindicato = (5/100.0 * salario_bruto)

valor_trabalho = ir + inss + sindicato
salario_liquido = salario_bruto - valor_trabalho

print("Seu salário bruto =", salario_bruto)

print("Valor dos impostos:")
print("IR: ", ir)
print("INSS: ", inss)
print("Sindicato: ", sindicato)

print("Seu salário liquido =", salario_liquido)

