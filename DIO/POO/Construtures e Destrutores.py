'''
    underline-2x '__' palavra-chave-reservada underline-2x '__'
    é um método especial;

    __init__ É um construtor, usado para inicializar valores;
    Inicia um objeto na classe... 
    É o primeiro a ser executado.  

    __del__ É um destrutor, quando o objeto não está mais 
    sendo usado, podemos 'destruí-lo' para liberar espaço 
    na memória;
    É executado por último, depois de todo processamento;
    Podemos forçar a destruição chamando a palavra reservada 
    'del'.

3 Exemplos:

Recursos externos: Se um objeto estiver utilizando recursos
externos, como arquivos, conexões de rede ou bloqueios, 
um destrutor pode ser usado para liberar esses recursos 
quando o objeto não for mais necessário. 
Por exemplo:

class Arquivo:
    def __init__(self, nome_arquivo):
        self.arquivo = open(nome_arquivo, 'r')

    def __del__(self):
        self.arquivo.close()    

Nesse exemplo, o destrutor fecha o arquivo aberto quando o 
objeto Arquivo é destruído, garantindo que os recursos sejam 
liberados adequadamente.
        
Logging e depuração: Em situações em que você deseja registrar
informações quando um objeto é destruído, um destrutor pode 
ser útil. Isso pode ser útil para fins de depuração e 
monitoramento. Por exemplo:

import logging

class ObjetoLog:
    def __init__(self, nome):
        self.nome = nome

    def __del__(self):
        logging.info(f'O objeto {self.nome} foi destruído.')

Nesse exemplo, o destrutor registra uma mensagem de log 
quando o objeto é destruído, permitindo rastrear o ciclo de 
vida do objeto.

Liberação de recursos personalizados: Se um objeto estiver 
usando recursos personalizados que não são automaticamente 
liberados pelo coletor de lixo, um destrutor pode ser usado 
para realizar a liberação adequada desses recursos. Isso pode 
ser útil em casos específicos, como quando há uma conexão 
com um hardware externo ou uma biblioteca que requer 
liberação EXPLÌCITA de recursos.
'''


class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print('Inicializando a classe..')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print('Removendo a instância da classe.')
        # 'pass' -> se não for comentado nada, ele só destroi  
        # e ninguém fica sabendo

    def latir(self):
        print('au au au')


def criar_cachorro():
    c = Cachorro('Lucky', 'Preto e caramelo', True)
    print(c.nome)


criar_cachorro()
# c = Cachorro('Chappie', 'caramelo')
# Cachorro.latir(c)  # c.latir()
# print('Olá mundo')
# del c
# print('Olá mundo')
# print('Olá mundo')
# print('Olá mundo')
# criar_cachorro()
