v_prod=float(input("Qual o valor do produto: "))
form=int(input("""Qual a forma de pagamento:
1-à vista no dinheiro ou cheque: 10% de desconto
2-à vista no cartão: 5% de desconto
3-2x no cartão: preço normal
4-3x ou mais no cartão: 20% de juros \n"""))
if form==1:
    print(" o preço do produto é {:.2f}".format(v_prod-(v_prod*0.1)))
elif form==2:
    print(" o preço do produto é {:.2f}".format(v_prod-(v_prod*0.05)))
elif form==3:
    print(" o preço do produto é {:.2f}".format(v_prod))
elif form ==4:
    print(" o preço do produto é {:.2f}".format(v_prod+(v_prod*0.2)))
else:
    print("essa opção é invalida")