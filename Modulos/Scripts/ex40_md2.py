def valor_nota(x):
    return int(input('voce digitou errado, escreva novamente:'))

a = int(input('numero 1:'))
if a>10:
    a = valor_nota(a)
b =  int(input('numero 2:'))
if b>10:
    b = valor_nota(b)
c =  int(input('numero 3:'))
if c>10:
    c = valor_nota(c)
d =  int(input('numero 4:'))
if d>10:
    d = valor_nota(d)

media= (a+b+c+d)/4
print('média é {}'.format(media))
if media<5.0:
    print("você foi reprovado")
elif media>5.0 and media<6.9:
    print("você está de recuperação")
elif media>7.0:
    print("você foi aprovado")


