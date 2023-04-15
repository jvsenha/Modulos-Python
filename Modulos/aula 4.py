
def valor_nota(x):
    return int(input('voce digitou errado, escreva novamente:'))

a = int(input('numero 1:'))
while a>10:
    a = valor_nota(a)
b =  int(input('numero 2:'))
while b>10:
    b = valor_nota(b)
c =  int(input('numero 3:'))
while c>10:
    c = valor_nota(c)
d =  int(input('numero 4:'))
while d>10:
    d = valor_nota(d)

media= (a+b+c+d)/4
print('média é {}'.format(media))


# nota = int(input('entre com a nota: '))
# while nota>10:
#    nota = int(input(' nota invalida, entre com a nota novamente: '))
#
#


# a = int(input('numero 1:'))
# for num in range(a+1):
#     div=0
#     for x in range (1, num+1):
#         rest = num % x
#         # print(x, rest)
#         if rest ==0:
#             div += 1
#     if div==2:
#         print(num)
#
#
#  for x in range(101):
#      print(x)4