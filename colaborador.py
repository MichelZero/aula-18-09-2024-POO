#
#
#  autor: Michel
# data: 18/09/2024

# importa a classe date da biblioteca datetime
from datetime import date

class Colaborador:
  def __init__(self, nome, anoNascimento = 0, cargo = "vendedor"):
    # anoNascimento é um parâmetro opcional caso não seja passado, o valor padrão é 0 
    # cargo é um parâmetro opcional caso não seja passado, o valor padrão é "vendedor"
    self.nome = nome
    self.anoNascimento = anoNascimento
    self.cargo = cargo
    # atributo hoje recebe a data atual   
    self.hoje = date.today()
    
  def calculaIdade(self):
    # o calculo da idade é feito subtraindo o ano de nascimento do ano atual 
    # self.hoje.year é o ano atual, self.anoNascimento é o ano de nascimento
    return f"sua idade é:", self.hoje.year - self.anoNascimento
  
  def calculaSalario(self):
    pass
  
  
# teste
Colaborador1 = Colaborador("pedro", 2005)
print(Colaborador1.calculaIdade())