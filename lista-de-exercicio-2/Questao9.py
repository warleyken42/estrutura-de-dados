num1 = int(input("Primeiro numero: "))
num2 = int(input("Segundo numero: "))
num3 = int(input("Terceiro numero: "))

print(num1,"-",num2,"-",num3)

if num3 > num2:
    auxiliar = num3
    num3 = num2
    num2 = auxiliar

if num2 > num1:
    auxiliar = num2
    num2 = num1
    num1 = auxiliar

if num3 > num2:
    auxiliar = num3
    num3 = num2
    num2 = auxiliar

print(num1,"-",num2,"-",num3)
