from datetime import date

nasc=int(input("Qual seu ano de nascimento:"))
ano = date.today().year
idade= ano-nasc
if  idade==18:
    print("você ja pode se alistar")
elif idade<18:
    print("você não pode se alistar, faltam {} anos".format(18-idade))
else:
    print("você ja passou do prazo de alistamento, devia ter se alistado a {} anos".format(idade-18))
    print(" seu alistamento foi em {}".format(ano-(idade-18)))
