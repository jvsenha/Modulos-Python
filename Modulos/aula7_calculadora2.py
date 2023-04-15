#classe: Sempre começa com letra Maiuscula.
class Calculadora:
    #inicializa valores
    def __init__(self):
      pass

    #metodos:Sempre começa com letra minuscula.
    def soma(self,valor_a,valor_b ):
        return valor_a + valor_b
    def sub(self,valor_a,valor_b):
        return valor_a -valor_b
    def mult(self,valor_a,valor_b):
        return valor_a * valor_b
    def div(self,valor_a,valor_b):
        return  valor_a / valor_b

calculadora = Calculadora()

print(calculadora.soma(10,2))
print(calculadora.sub(10,2))
print(calculadora.div(10,2))
print(calculadora.mult(10,2))
