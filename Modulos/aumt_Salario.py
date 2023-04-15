sal=float(input('qual o valor do seu salario? '))
if sal<=1250:
    sal=sal+(sal*0.15)
else:
    sal = sal + (sal * 0.1)
print('seu novo salario é {:.2f}'.format(sal))
