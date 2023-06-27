"""
O polimorfismo é um conceito composto usado junto a herança em que
um objeto vai possuir diversas atribuições, neste exemplo usamos o
polimorfismo no método 'plano_voo' onde a função trata qualquer objeto
com o mesmo funcionamento
pag 136
"""


class Passaro:
    def voar(self):
        print('voando...')


class Pardal(Passaro):
    def voar(self):
        super().voar()


class Avestruz:
    def voar(self):
        print('Avestruz não voa')


def plano_voo(obj):
    obj.voar()


plano_voo(Pardal())
plano_voo(Avestruz())
