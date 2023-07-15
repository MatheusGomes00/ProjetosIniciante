import sys
sys.stdout.reconfigure(encoding='utf-8')

"""
O polimorfismo é usado junto a herança onde um mesmo método pode 
receber comportamentos diferentes, neste exemplo
usamos o polimorfismo no método 'voar' onde a função recebe diferentes
atribuições/comportamentos, dependendo da sua classe, então o conceito
é aplicado na função 'plano_voo' que recebe um objeto e chama outra
função, que no caso é o voar. Todo objeto que for passado para a função
'plano_voo' precisa necessariamente possuir o método voar.
É basicamente uma função que recebe um objeto e chama um método 
polimórfico, que vai receber diferentes comportamentos e atribuições. 
Um exemplo de polimorfismo na prórpia linguagem python é o método 'len'
que retorna diferentes valores conforme sua verificação ... 


"""


class Passaro:
    def voar(self):
        print('voando...')


class Pardal(Passaro):
    def voar(self):
        super().voar()


class Avestruz:
    def voar(self):
        print("Avestruz não voa.")


# FIXME: exemplo ruim do uso de herança para 'ganhar/receber' o método voar
class Aviao:
    def voar(self):
        print("Avião decolando ...")

def plano_voo(passaro):
    passaro.voar()


plano_voo(Pardal())
plano_voo(Avestruz())
jhony = Avestruz()
plano_voo(jhony)
helicoptero = Aviao()
plano_voo(helicoptero)
