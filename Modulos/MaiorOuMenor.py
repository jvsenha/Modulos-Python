num1=int(input('digite o 1º numero:'))
num2=int(input('digite o 2º numero:'))
num3=int(input('digite o 3º numero:'))
menor=num1
if num2<num1 and num2<num3:
    menor=num2
if num3<num2 and num3<num1 :
    menor=num3
maior=num1
if num2>num1 and num2>num3:
    maior = num2
if num3>num1 and num3>num2:
    maior = num3
print('o maior é {}'.format(maior))
print('o menor é {}'.format(menor))