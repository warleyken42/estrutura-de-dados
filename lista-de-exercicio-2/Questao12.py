horas = int(input("Digite quanto ganha por hora: "))
quantidade_horas = int(input("Digite o numero de horas trabalhadas:"))

salario_bruto = quantidade_horas * horas

cinco_porcento = (5 / 100.0) * salario_bruto
dez_porcento = (10/ 100.0) * salario_bruto
onze_porcento = (11 / 100.0) * salario_bruto
vinte_porcento = (20 / 100.0) * salario_bruto

if salario_bruto <= 900:       
       print("Seu salario bruto  : R$ {}".format(salario_bruto))
       print("(-)  IR  (5%)      : R$ {}".format(0))
       print("(-) INSS (10%)     : R$ {}".format(0))
       print("FGTS     (11%)     : R$ {}".format(0))
       print("Salário Liquido    : R$ {}".format(salario_bruto))
elif salario_bruto >= 900 and salario_bruto <= 1500:
       print("Seu salario bruto  : R$ {}".format(salario_bruto))
       print("(-)  IR  (5%)      : R$ {}".format(cinco_porcento))
       print("(-) INSS (10%)     : R$ {}".format(dez_porcento))
       print("FGTS     (11%)     : R$ {}".format(onze_porcento))
       print("Total de descontos : R$ {}".format(cinco_porcento + dez_porcento))
       print("Salário Liquido    : R$ {}".format(salario_bruto - (cinco_porcento + dez_porcento))) 
elif salario_bruto > 1500 and salario_brunto <= 2500:
       print("Seu salario bruto  : R$ {}".format(salario_bruto))
       print("(-)  IR  (5%)      : R$ {}".format(cinco_porcento))
       print("(-) INSS (10%)     : R$ {}".format(dez_porcento))
       print("FGTS     (11%)     : R$ {}".format(onze_porcento))
       print("Total de descontos : R$ {}".format(dez_porcento + dez_porcento))
       print("Salário Liquido    : R$ {}".format(salario_bruto - (dez_porcento + dez_porcento))) 
elif salario_bruto > 2500:
       print("Seu salario bruto  : R$ {}".format(salario_bruto))
       print("(-)  IR  (5%)      : R$ {}".format(cinco_porcento))
       print("(-) INSS (10%)     : R$ {}".format(dez_porcento))
       print("FGTS     (11%)     : R$ {}".format(onze_porcento))
       print("Total de descontos : R$ {}".format(vinte_porcento + dez_porcento))
       print("Salário Liquido    : R$ {}".format(salario_bruto - (vinte_porcento + dez_porcento)))