nota1 = float(input("Digite o valor da primeira nota: "))
nota2= float(input("Digite o valor da segunda nota: "))

media = (nota1 + nota2)/2

if media >= 9 and media <= 10:
    print("A nota da primeira prova: {} ".format(nota1))
    print("A nota da segunda prova: {} ".format(nota2))
    print("A media é: {}".format(media))
    print("Você tirou A")
    print("Você foi aprovado!!")
elif media >= 7.5 and media < 9:
    print("A nota da primeira prova: {} ".format(nota1))
    print("A nota da segunda prova: {} ".format(nota2))
    print("A media é: {}".format(media))
    print("Você tirou B")
    print("Você foi aprovado!!")
elif media >= 6.0 and media < 7.5:
    print("A nota da primeira prova: {} ".format(nota1))
    print("A nota da segunda prova: {} ".format(nota2))
    print("A media é: {}".format(media))
    print("Você tirou C")
    print("Você foi aprovado!!")
elif media >= 4 and media < 6:
    print("A nota da primeira prova: {} ".format(nota1))
    print("A nota da segunda prova: {} ".format(nota2))
    print("A media é: {}".format(media))
    print("Você tirou D")
    print("Você foi reprovado!!")
elif media < 4:
    print("A nota da primeira prova: {} ".format(nota1))
    print("A nota da segunda prova: {} ".format(nota2))
    print("A media é: {}".format(media))
    print("Você tirou E")
    print("Você foi reprovado!!") 