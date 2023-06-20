num= int(input("digite um nomero inteiro: "))
print(""" Escolha uma das bases par conversão:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL""")
opc=int(input("Sua escolha:"))
if opc==1:
    print("{} convertido para BINARIO é igual a {}".format(num, bin(num)[2:]))
elif opc==2:
    print("{} convertido para OCTAL é igual a {}".format(num, oct(num)[2:]))
elif opc==3:
    print("{} convertido para HEXADECIMAL é igual a {}".format(num, hex(num)[2:]))
else:
    print("essa opção é invalida")