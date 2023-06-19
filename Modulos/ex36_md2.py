value = float(input("qual o valor da casa: "))
sal = float(input("qual seu salaraio: "))
temp= int(input("quanto tempo em você pretenmde pagar (em anos): "))
vpm= value/(temp*12)
if vpm<=(sal * 0.3):
    print("seu emprestimo foi aprovado \n você pagara {} parcelas de {:.2f}". format((temp*12),vpm))
else:
    print("seu emprestimo não foi aprovado")


