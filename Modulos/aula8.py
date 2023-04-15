from aula7_televisao import Televisao
from aula8_conta_letra import  conta_letras

print(__name__)
if __name__ == '__main__':
    tv = Televisao()
    print(tv.ligada)
    tv.power()
    print(tv.ligada)
    lista_animal=['cachorro', 'gato', 'elefante','lobo', 'arara']
    total_letras= conta_letras(lista_animal)
    print('o total de letras é: {}'. format(total_letras))