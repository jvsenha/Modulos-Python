import random
from cores import color
c= color()
def Jogo(play,nome):
    items = ('pedra', 'papel', 'tesoura')
    comp = random.randint(0, 2)
    print("\n")
    print(" python: {} vs  você: {}".format(items[comp], items[play]))
    if (comp ==2 and play==1) or (comp ==1 and play==0) or (comp ==0 and play==2):
        print('{}Que pena, você perdeu.{}'.format(c.cores['falha'],c.cores['limp']))

    elif  (play ==2 and comp==1) or (play ==1 and comp==0) or (play ==0 and comp==2):
        print('{}Parabens {}, Você acertou!!{}'.format(c.cores['sucesso'], nome, c.cores['limp']))

    elif comp==play:
        print('empatamos!!'.format(nome))
    print("\n")
    again = str(input('Quer jogar de novo? S(sim)/N(Não)').lower())
    print("\n")
    while again == 's':
        play = int(input("""{} oque você escolhe:
        [0] pedra
        [1] papel 
        [2] tesoura
        {}""" .format(c.cores['PeB'],c.cores['limp'],nome)))
        play = (Jogo(play, nome))








nome= str(input('qual seu nome? ').title().strip())
print("""
      """)
print("""{} Olá {}, Eu Sou o python, vamos jogar jockeypô?{}
{}Escolha pedra, papel, ou tesoura.{}""".format(c.cores['azul'],nome,c.cores['limp'],c.cores['azul'],c.cores['limp']))
print("""
      """)
play = int(input("{} oque você escolhe: \n [0] pedra \n [1] papel \n [2] tesoura \n Sua escolha: {} ".format(c.cores['azul'], c.cores['limp'], nome)))
play = (Jogo(play, nome))