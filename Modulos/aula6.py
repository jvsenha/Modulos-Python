conjunto = {1,2,3,4}
conjunto2 = {2,4,5,6}
# print(conjunto)
# conjunto.add(5)
# print(conjunto)
# conjunto.remove(2)
# print(conjunto)
conjunto_uniao= conjunto.union(conjunto2)
print('união: {}'.format(conjunto_uniao))
conjunto_intersecao= conjunto.intersection(conjunto2)
print('intersecção: {}'.format(conjunto_intersecao))
conjunto_dif= conjunto.difference(conjunto2)
print('deferença : {}'.format(conjunto_dif))
conjunto_dif2= conjunto2.difference(conjunto)
print('deferença 2: {}'.format(conjunto_dif2))
conjunto_symdif= conjunto2.symmetric_difference(conjunto)
print('deferença simetrica: {}'.format(conjunto_symdif))

conjunto3 = {1,2,3}
conjunto4 = {1,2,3,4,5,6}
conjunto_subset =conjunto3.issubset(conjunto4)
print(conjunto_subset)
conjunto_subset =conjunto4.issubset(conjunto3)
print(conjunto_subset)
conjunto_subset2 =conjunto4.issuperset(conjunto3)
print(conjunto_subset2)
conjunto_subset2 =conjunto3.issuperset(conjunto4)
print(conjunto_subset2)

lista=['cachorro', 'gato', 'gato', 'elefante']
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais= list(conjunto_animais)
print(lista_animais)