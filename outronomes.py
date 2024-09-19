#
#
#  autor: Michel
# data: 18/09/2024

class OutroNome:
  # construtor da classe OutroNome 
  # o primeiro parâmetro é aula, que é uma referência a classe OutroNome
  # o correto seria self, mas para mostrar que o nome do primeiro parâmetro pode ser qualquer um, foi colocado aula
  def __init__(aula, name, age): 
    # atributos da classe OutroNome devem ser referenciados com aula
    # o correto seria self, mas para mostrar que o nome do primeiro parâmetro pode ser qualquer um, foi colocado aula
    aula.name = name  
    aula.age = age  
    
    
# instancia 
from outronomes import OutroNome

outro1 = OutroNome("Michel", 56)

print(f"nome -> {outro1.name}")