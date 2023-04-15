import random
from cores import color
c= color()
def Jogo(numP,nome):
    num = random.randint(0, 5)
    print("""
                   """)
    if num != numP:
        print('{}--'.format(c.cores['falha']) * 50)
        print('{}Que pena, você errou'.format(c.cores['falha']))
        print('--' * 50)
        print('{}'.format(c.cores['limp']))
    else:
        print('{}--'.format(c.cores['sucesso']) * 50)
        print('Parabens {}, Você acertou!!'.format(nome))
        print('--' * 50)
        print('{}'.format(c.cores['limp']))
    print("""
                 """)
    again = str(input('Quer jogar de novo? S(sim)/N(Não)').lower())
    print("""
          """)
    while again == 's':
        numP = int(input('{} qual numero Eu pensei?{} '.format(c.cores['PeB'],c.cores['limp'],nome)))
        numP = (Jogo(numP, nome))

nome=str(input('qual seu nome? ').title().strip())
print("""
      """)
print("""{}Olá {}, Eu Sou o python e Vou escolher um numero de 0 a 5,{}
{}Tente adivinhar qual o numero que Eu escolhi.{}""".format(c.cores['azul'],nome,c.cores['limp'],c.cores['azul'],c.cores['limp']))
print("""
      """)
numP = int(input('{} qual numero Eu pensei?{}'.format(c.cores['azul'],c.cores['limp'],nome)))
numP = (Jogo(numP, nome))

