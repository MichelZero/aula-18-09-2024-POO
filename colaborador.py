#
#
#  autor: Michel
# data: 18/09/2024

from datetime import date

class Colaborador:
  def __init__(self, nome, anoNascimento = 0, cargo = "vendedor"):
    self.nome = nome
    self.anoNascimento = anoNascimento
    self.cargo = cargo
    self.hoje = date.today()
    
  def calculaIdade(self):
    return f"sua idade é:", self.hoje.year - self.anoNascimento
  
  def calculaSalario(self):
    pass
  
  
# teste
Colaborador1 = Colaborador("pedro", 2005)
print(Colaborador1.calculaIdade())