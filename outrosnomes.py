#
#
#  autor: Michel
# data: 18/09/2024

class OutroNome:
  def __init__(aula, name, age):
    aula.name = name
    aula.age = age
    
    
# instancia 
from outrosnomes import OutroNome

outro1 = OutroNome("Michel", 56)

print(f"nome -> {outro1.name}")