vl = int(input("qual a velocidade do carro em Km/H? "))
if vl>80:
    multa= (vl-80)*7
    print("você foi multado em {}R$".format(multa))
else:
    print("você estava no limite de velocidade")