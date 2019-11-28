import os
class Carro:
  
  def __init__(self, nome, consumo, capacidade):
    self.nome = nome  
    self.consumo = abs(float(consumo))
    self.capacidade = abs(float(capacidade))
    self.combustivel = float(0)
  
  def andar(self, distancia):
    combustivel_necessario = distancia / self.consumo
    distancia_maxima = self.combustivel * self.consumo
    return [self.combustivel - combustivel_necessario, distancia_maxima]
  
  def nivel_gasolina(self):
    return self.combustivel
  
  def adicionar_gasolina(self, combustivel):
    self.combustivel += abs(combustivel)

def menu(L,carro):
  if carro != None:
    print("Carro selecionado: {}".format(carro.nome))
  
  menu_opcoes = input("-=-=-=-=-=-=-=-= Menu de Opções -=-=-=-=-=-=-=-=\n"
                      "| 1) Criar um novo veículo                      |\n"
                      "| 2) Selecionar um veículo                      |\n"
                      "| 3) Dirigir                                    |\n"
                      "| 4) Abastecer                                  |\n"
                      "| 5) Mostrar quantidade de gasolina no tanque   |\n"
                      "| 6) Exibir lista de veículos                   |\n"
                      "| 7) Excluir o veículo selecionado              |\n"
                      "| 8) Encerrar o programa                        |\n"
                      "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"
                      "|=> Escolha uma opção: ")
  os.system('clear')
  if menu_opcoes in ["1"]:
    nome = input("Nome do veículo: ")
    consumo = input("Quilometragem por litro: ")
    capacidade= input("Capacidade do tanque: ")
    L.append(Carro(nome,consumo,capacidade))
    print("")
    menu(L,carro)
    return
    os.system('clear')
  elif menu_opcoes in ["2"]:
    if L == []:
      print("Não tem carro")
      print("")
      menu(L,carro)
      return
    t = input("Escolha um veículo: ")
    for x in L:
      if t == x.nome:
          print("")
          menu(L,x)
          return  
    print("Este carro não existe!")
    print("")
    menu(L,carro)
    return
    os.system('clear')  
  elif menu_opcoes in ["3"]:
    if carro == None:
      print("É necessário selecionar um carro!")
      print("")
      menu(L,carro)
      return
    elif carro.combustivel == 0:
      print("Não há combustível no tanque!")
      print("")
      menu(L,carro)
      return
    else:  
      km = float(input("Digite a distância a ser percorrida: "))
      if carro.andar(km)[0] < 0:
        print ("Você andou {%:.2f} km. Precisa abastecer {%:.2f} litro(s) de combustível para completar o percurso".format(carro.andar(km)[1],-carro.andar(km)[0]))
        carro.combustivel = 0.0
      else:
        carro.combustivel = carro.andar(km)[0]      
    print("")
    menu(L,carro)
    return
  elif menu_opcoes in ["4"]:
    if carro == None:
      print("É necessário selecionar um carro!")
      print("")
      menu(L,carro)
      return
    litros = float(input("Digite a quantidade de combustível a ser adicionada: "))
    if litros + carro.combustivel > carro.capacidade:        
      print ("O tanque do veículo está cheio ou não suporta esta quantidade de combustível!")      
    else:
        carro.adicionar_gasolina(litros)
    print("")
    menu(L,carro)
    return
    os.system('clear')
  elif menu_opcoes in ["5"]:
    if carro == None:
      print("É necessário selecionar um carro!")
      print("")
      menu(L,carro)
      return
    os.system('clear')
    print ("Nível atual de combustível: {}".format(carro.nivel_gasolina()))
    print("")
    menu(L,carro)
    return  
  elif menu_opcoes in ["6"]:
    if L == []:
      print("Não tem carros!")
      print("")
      menu(L,carro)
      return
    M = []
    for i in L:
      M.append(i.nome)
    print (M)
    print("")
    menu(L,carro)
    return
    os.system('clear')
  elif menu_opcoes in ["7"]:
    if carro == None:
      print("É necessário selecionar um carro!")
      print("")
      menu(L,carro)
      return
    L.remove(carro)
    print("")
    menu(L,None)
    return
    os.system('clear')
  elif menu_opcoes in ["8"]:
    return
  else:
    print("opção inválida!")
    print("")
    menu(L,carro)
    return

menu([], None)