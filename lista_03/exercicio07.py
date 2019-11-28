class Tamagotchi:
  def __init__(self, nome, fome = "100", saude = "100", idade = "0", humor = "100"):
    self.nome = nome
    self.fome = fome
    self.saude = saude
    self.idade = idade
    self.humor = humor
  
  def alterar_nome(self,nome):
    self.nome = nome

  def alterar_fome(self,fome):
    self.fome = fome

  def alterar_saude(self,saude):
    self.saude = saude

  def alterar_idade(self,idade):
    self.idade = idade
  
  def alterar_humor(self,fome, saude):
    self.humor = ((fome*3)+(saude*2))/3*2*1
  
  def retornar_nome(self):
    return self.nome
  
  def retornar_fome(self):
    return self.fome
  
  def retornar_saude(self):
    return self.saude
  
  def retornar_idade(self):
    return self.idade
  
  def retornar_humor(self):
    return self.humor
  
  def imprimir(self):
      print("Nome: {}\nNivel/Fome: {}\nNivel/Saude: {}\nIdade: {}\nHumor: {}".format(self.nome, self.fome, self.saude, self.idade, self.humor))

bichinho = Tamagotchi(input("Dê o nome para o Tamagotchi: "))
bichinho.imprimir()
print("\n")
bichinho.alterar_nome("LUCAS")
bichinho.imprimir()
print("\n")
bichinho.alterar_fome(40)
bichinho.alterar_saude(50)
bichinho.alterar_idade(10)
bichinho.imprimir()

while True:

  print(" _____OPÇÕES______")
  print("|1 - Cuidados     |")
  print("|2 - Informações  |")
  print("|3 - Sair do Jogo |")
  print("|_________________|")
  selec = input("Selecionar: ")
  if selec == "1":
    print(" _____OPÇÕES______")
    print("|1 - Alimentar    |")
    print("|2 - Dar Banho    |")
    print("|3 - Brincar      |")
    print("|4 - Dormir       |")
    print("|5 - Sair do Jogo |")
    print("|_________________|")
    selec = input("Selecionar: ")
    if selec == "1":
      print(" _________OPÇÕES________")
      print("|1 - Lazanha            |")
      print("|2 - Arroz e Feijão     |")
      print("|3 - Ovo de Codornia    |")
      print("|4 - Sair do Jogo       |")
      print("|_______________________|")
      selec = input("Selecionar: ")
      if selec == "1":
        pass
      elif selec == "2":
        pass
      elif selec == "3":
        pass
      elif selec == "4": 
        print("Saindo ...")
        break
      else:
        print("informe uma opção valida")
    elif selec == "2":
      pass
    elif selec == "3":
      pass
    elif selec == "4":
      pass
    elif selec == "5": 
      print("Fim do Jogo!")
      print("Saindo ...")
      break
    else:
      print("informe uma opção valida")
  elif selec == "2":
    bichinho.imprimir()
  elif selec == "3":
    print("Fim do Jogo!")
    print("Saindo ...")
    break
  else:
    print("informe uma opção valida")

#DEPOIS IMPLEMENTAR OS ATRIBUTOS QUE FORAM COLOCADOS EXTRAS, FIZ ESSE PROGRAMA CONFORME O QUE EU JA HAVIA FEITO EM JAVA