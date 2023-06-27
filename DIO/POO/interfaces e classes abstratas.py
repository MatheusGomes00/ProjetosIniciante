from abc import ABC, abstractmethod

""" Interface define O QUE uma classe deve fazer e não COMO (todo padrão de execução) """
"""Métodos abstratos não possuem corpo, ele obriga todas as classes filhas a receber os métodos da mãe"""
"""Toda classe filha deve implementar os métodos da classe mãe"""


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print('Ligando a TV')
        print('Ligada!')

    def desligar(self):
        print('Desligando a TV...')
        print('Desligada')

    def marca(self):
        return "LG"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado ...")
        print("Ligado")

    def desligar(self):
        print('Desligando Ar Condicionado...')
        print('Desligado')

    def marca(self):
        return "LG"


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca())
controle2 = ControleArCondicionado()
controle2.ligar()
controle2.desligar()
print(controle2.marca())
