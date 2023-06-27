# underline alguma coisa underline é um método especial
# __init__ é um construtor, usado para inicializar valores de um objeto na classe... inicializa a classe
# __del__ é um destrutor, quando o objeto não está mais sendo usado, podemos 'destruí-lo' para liberar espaço na memória
class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print('Inicializando a classe..')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print('Removendo a instância da classe.')
    def latir(self):
        print('au au au')


def criar_cachorro():
    c = Cachorro('Lucky', 'Preto e caramelo', True)
    print(c.nome)


c = Cachorro('Chappie', 'caramelo')
Cachorro.latir(c)  # c.latir()
print('Olá mundo')
del c
print('Olá mundo')
print('Olá mundo')
print('Olá mundo')
criar_cachorro()
