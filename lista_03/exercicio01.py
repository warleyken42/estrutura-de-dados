class Bola:
  def __init__(self, cor, circuferencia, material):
    self.cor = cor
    self.circuferencia = circuferencia
    self.material = material
  def troca_cor(self, cor):
    self.cor = cor
  def mostra_cor(self):
    print("Minha cor e {} feita de {}".format(self.cor, self.material))


bola = Bola("azul", 2, "Couro")
bola.mostra_cor()
bola.troca_cor("verde")
bola.mostra_cor()
bola.troca_cor("Amarelo")
bola.mostra_cor()
