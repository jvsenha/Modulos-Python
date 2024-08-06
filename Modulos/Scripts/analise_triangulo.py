from cores import color
c= color()
lad1=int(input('digite o 1º Lado:'))
lad2=int(input('digite o 2º Lado:'))
lad3=int(input('digite o 3º Lado:'))
if  lad1 < (lad2 + lad3) and lad2 < (lad1 + lad3)  and lad3 < (lad1 + lad2):
    print('{}você pode formar um tringulo{}'.format(c.cores['sucesso'],c.cores['limp']))
else :
    print('{}você não pode formar um tringulo{}'.format(c.cores['falha'],c.cores['limp']))