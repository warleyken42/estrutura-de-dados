class Televisao:
    
    def __init__(self, canal = "1", volume = "10"):
      self.canal = canal
      self.volume = volume
    
    def canal(self):
        return self.canal

    def escolher_canal(self, numero):
      if numero > 0 and numero <= 30:
        self.canal = numero
      else:
        print("Canal fora do ar!\nTente outro canal")

    def volume(self):
      return self.volume

    def volume(self, numero):
      if numero >=0 and numero <= 100:
        self.volume = numero
      else: 
        print("O volume deve ser entre 0 e 100")


    def mudar_canal(self):
      numero = input("Mudar para o Canal: ")
      self.canal = numero

    def mudar_volume(self):
      numero = input("Mudar para o Volume: ")
      self.volume = numero

    def __str__(self):
      return "Canal: {}\nVolume: {}\n".format(self.canal, self.volume)

tv1 = Televisao()


while True:
  print(tv1)

  print(" _____OPÇÕES______")
  print("|1 - MUDAR CANAL  |")
  print("|2 - MUDAR VOLUME |")
  print("|3 - DESLIGAR TV  |")
  print("|_________________|")
  selec = input("Selecionar: ")

  if selec == "1":
    tv1.mudar_canal()
    print("\n")
  elif selec == "2":
    tv1.mudar_volume()
    print("\n")
  elif selec == "3":
    print("Desligando ...")
    break
  else:
    print("Selecione uma opcão válida!")