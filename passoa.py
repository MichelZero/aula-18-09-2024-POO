#
#
#  autor: Michel
# data: 18/09/2024

class Pessoa:
  nome1 = "padrão" 
  #nome1 faz parte do escopo global da classe Pessoa 
  #nome1 é instanciáveis por qualquer método da classe Pessoa 
  #nome1 é acessível por qualquer instância de Pessoa
  
  def __init__(self, nome2):
    self.nome2 = nome2
    #nome2 faz parte do escopo do método inicializador ou construtor
    #nome2 é acessível dentro e fora deste método
    #nome2 pode ser instanciado de fora da classe
    nome3 = "usuário"
    #nome3 faz parte do escopo do método inicializador ou construtor
    #nome3 é acessível somente dentro desse método