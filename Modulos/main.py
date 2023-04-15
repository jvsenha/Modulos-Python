a = int(input('numero 1:'))
b=  int(input('numero 2:'))
soma = a+b
sub= a-b
mut= a*b
rest= a%b
div= a/b
resultado = ('soma {} \n Subtração: {} \n Multiplicação: {} \n resto: {} \n'
      ' divisão: {} '
      . format(soma, sub, mut, rest, div))
print(resultado)