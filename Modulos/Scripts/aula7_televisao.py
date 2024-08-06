class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal=2
    def power(self):
        if self.ligada:
            self.ligada= False
        else:
            self.ligada = True
    def canal_aumt(sefl):
        if sefl.ligada:
            sefl.canal += 1

    def canal_dim(sefl):
        if sefl.ligada:
            sefl.canal -= 1

if __name__ =='__main__':
    tv = Televisao()
    print('televisão está ligada: {}'.format(tv.ligada))
    tv.power()
    print('televisão está ligada: {}'.format(tv.ligada))
    tv.power()
    print('televisão está ligada: {}'.format(tv.ligada))
    tv.power()
    print('televisão está ligada: {}'.format(tv.ligada))
    print('Canal: {}'.format(tv.canal))
    tv.canal_aumt()
    tv.canal_aumt()
    print('Canal: {}'.format(tv.canal))
    tv.canal_dim()
    print('Canal: {}'.format(tv.canal))