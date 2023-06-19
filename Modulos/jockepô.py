import random
from cores import color
c= color()
def Jogo(escP,nome):
    esc = random.choice("pedra","papel","tesoura")

    print("\n")

    print("{}vs{}".format(esc, escP))
    if (esc =="tesoura" and escP=="papel") or (esc =="papel" and escP=="pedra") or (esc =="pedra" and escP=="tesoura"):

        print('{}Que pena, você perdeu.'.format(c.cores['falha']))

    elif  (escP =="tesoura" and esc=="papel") or (escP =="papel" and esc=="pedra") or (escP =="pedra" and esc=="tesoura"):

        print('Parabens {}, Você acertou!!'.format(nome))

    elif esc==escP:

        print('empatamos!!'.format(nome))
    print("\n")
    again = str(input('Quer jogar de novo? S(sim)/N(Não)').lower())
    print("\n")
    while again == 's':
        escP = str(input('{} oque você escolhe: pedra, papel ou tesoura? {} '.format(c.cores['PeB'],c.cores['limp'],nome)))
        escP = (Jogo(escP, nome))








nome=str(input('qual seu nome? ').title().strip())
print("""
      """)
print("""{} Olá {}, Eu Sou o python, vamos jogar jockeypô?{}
{}Escolha pedra, papel, ou tesoura.{}""".format(c.cores['azul'],nome,c.cores['limp'],c.cores['azul'],c.cores['limp']))
print("""
      """)
escP = str(input('{} oque você escolhe?{}'.format(c.cores['azul'],c.cores['limp'],nome)))
escP = (Jogo(escP, nome))
