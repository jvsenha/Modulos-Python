peso=float(input("qual a seu peso: "))
alt=float(input("qual a sua altura: "))
imc=peso/(alt**2)
if imc<18.5:
    print("abaixo do peso, seu imc é {:.2f}".format(imc))
elif imc>=18.5 and imc<25:
    print("peso ideal, seu imc é {:.2f}".format(imc))
elif imc>=25 and imc<30:
    print("sobrepeso, seu imc é {:.2f}".format(imc))
elif imc>=30 and imc<40:
    print("obesidade, seu imc é {:.2f}".format(imc))
else:
    print("obesidade morbida, seu imc é {:.2f}".format(imc))