from datetime import date

nasc=int(input("Qual seu ano de nascimento:"))
ano = date.today().year
idade= ano-nasc
if idade<=9:
    print("mirim")
if idade >= 9 and idade<=14 :
    print("infantil")
if idade >= 14 and idade<=19 :
    print("junior")
if idade==20 :
    print("sênior")
if idade>20:
    print("master")