# Construções de métodos, funções e classes em python
# Para usar os métodos precisamos definilos usando o "def"

#Class por conversão começa com letra maiúscula.

class Calculadora:
  def _init(self, num1, num2):
    self.valorA = num1
    self.valorB = num2
  def soma(self):
    return self.valorA + self.valorB

  def sub(self):
    return self.valorA - self.valorB
    
  def mult(self):
    return self.valorA * self.valorB

  def div(self):
    return self.valorA / self.valorB

calculadora = Calculadora(10, 2)
# print(calculadora.valorA)
# print(calculadora.valorB)

  # print(soma(4, 5))
  # print(sub(2554,1582))
  # print(mult(52, 25))
  # print(div(754, 52))