d=float(input('qual a distancia da viagem: '))
if d<=200:
    p=d*0.50
    print('sua viagem vai custar: R${:.2f}'.format(p))
else:
    p = d * 0.45
    print('sua viagem vai custar: R${:.2f}'.format(p))
