conta_letras = lambda lista: [len(x) for x in lista]

lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']
print(conta_letras(lista_animal))

calculadora = {
    'sum': lambda  a, b: a+b,
    'sub': lambda  a, b: a-b,
    'mult': lambda  a, b: a*b,
    'div': lambda  a, b: a/b
}

soma= calculadora['sum']
mult= calculadora['mult']
print(soma(10,5))

