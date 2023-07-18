from abc import ABC, abstractmethod

""" 
Interface define O QUE uma classe deve fazer e não COMO 
(todo padrão de execução).
O conceito de interface é definir um contrato, onde são 
declarados os métodos (o que deve ser feito) e suas 
respectivas assinaturas. Em Python utilizamos classes 
abstratas para criar contratos. Classes abstratas não 
podem ser instanciadas.

A interface serve para compor um comportamento na minha classe.

Métodos abstratos não possuem corpo, ele obriga todas as 
classes filhas a receber os métodos da mãe. Toda classe filha 
deve implementar os métodos da classe mãe

Por padrão, o Python não fornece classes abstratas. Existe um
módulo que fornece a base para definir as classes abstratas, e
o nome do módulo é 'ABC'. O 'ABC' funciona decorando métodos da
classe base como abstratos e, em seguida, registrando classes
concretas como implementações da base abstrata. Um método se 
torna abstrato quando decorado com @abstractmethod.

"""

class ControleRemoto(ABC):
# a classe extende o módulo/biblioteca ABC, obrigando as 
# instâncias da classe receber o decorador @abstractmethod
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
