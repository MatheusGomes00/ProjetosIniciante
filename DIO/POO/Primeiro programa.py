class Moto:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print('bibi bibi bibiiiiii')

    def parar(self):
        print('Parando moto...')
        print('Moto parada!')

    def correr(self):
        print('Randandandandan')

    # criamos esta função para tornar legível como foi instanciado determinado objeto nesta classe
    # o método __str__ retorna uma string por padrão.
    # se não for criada esta função o retorno de print(m2) por exemplo será: <__main__.Moto object at 0x0000026A3198A170>
    # dessa forma precisamos sempre atualizar se houver alguma alteração
    # def __str__(self):
    #     return f'Moto: Cor={self.cor}, Ano={self.ano}, Modelo={self.modelo}, Valor={self.valor}'
    # desta outra forma é atualizado automático sempre que alguma alteração é feita
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        # self.__class__.__name__ -> é usado para mostar o nome da classe do objeto instanciado
        # [f'{chave}={valor}' for chave, valor in self.__dict__.items()] -> list comprehension
        # faz a compressão de um laço e repetição para apresentar em forma de dicionário, {chave}={valor}
        # in self.__dict__ -> método/atributo da classe utilizado para selecionar os dicionários da classe
        # .items() -> faz com que os item sejam representados sem os colchetes {} e aspas "" que um dicionário gera.
        # ', '.join -> separa cada dicionário por uma virgula e espaço
m1 = Moto('vermelho', 'kawasaki', 2022, 45000)
m2 = Moto('azul', 'honda', 2005, 8000)
m1.buzinar()
m1.correr()
m1.parar()
# conseguimos acessar os atributos do objeto
print(m1.cor, m1.ano, m1.valor, m1.modelo)
Moto.buzinar(m1)
print(m2)  # para saber como foi instanciado determinado objeto, o que tem dentro da classe x no objeto y
