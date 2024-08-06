#classe: Sempre começa com letra Maiuscula.
class Calculadora:
    #inicializa valores
    def __init__(self, num1,num2):
        self.valor_a = num1
        self.valor_b = num2
    #metodos:Sempre começa com letra minuscula.
    def soma(self):
        return self.valor_a + self.valor_b
    def sub(self):
        return self.valor_a - self.valor_b
    def mult(self):
        return self.valor_a * self.valor_b
    def div(self):
        return  self.valor_a / self.valor_b

if __name__=='__main__':
    calculadora = Calculadora(10, 2)
    print(calculadora.valor_a)
    print(calculadora.soma())
    print(calculadora.sub())
    print(calculadora.div())
    print(calculadora.mult())
