soma = 0
num = 0
for c in range(1,501,2):
    if c%3==0:
        soma+=c
        num+=1
print(" soma entre os {} números que são múltiplos de três e que se encontram"
      " no intervalo de 1 até 500 é {}".format(num, soma) )