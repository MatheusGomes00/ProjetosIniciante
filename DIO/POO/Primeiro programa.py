'''
def __init__(self, parâmetros...) -> construtor que inicia a classe e suas instancias de objeto
    self.caracteristica = caracteristica -> instancia de objeto ou as características da classe

def comportamento(self): -> método da classe para tratar comportamento
'''
class Moto:  # nome da classe sempre começa com letra maíuscula
    def __init__(self, cor, modelo, ano, valor): 
        self.cor = cor  
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):  # método
        print('bibi bibi bibiiiiii')

    def parar(self):
        print('Parando moto...')
        print('Moto parada!')

    def correr(self):
        print('Randandandandan')

    # criamos a seguinte função para tornar legível como foi instanciado determinado objeto nesta classe
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
        # in self.__dict__ -> método/atributo de classe utilizado para selecionar os dicionários da classe
        # .items() -> faz com que os item sejam representados sem os colchetes {} e aspas "" que um dicionário gera.
        # o método items() é utilizado para iterar itens de um dicionário e gerar tuplas com pares chave: valor
        # ', '.join -> separa cada dicionário por uma virgula e espaço



m1 = Moto('vermelho', 'kawasaki', 2022, 45000)  # instanciado o objeto m1 na classe moto
m2 = Moto('azul', 'honda', 2005, 8000)
m1.buzinar()  # chamada de método/comportamento da classe moto
m1.correr()
m1.parar()
# conseguimos acessar os atributos do objeto
print(m1.cor, m1.ano, m1.valor, m1.modelo)  # forma não convencional de acessar as instancias do objeto
Moto.buzinar(m1)
print(m2) # forma convencional de acessar as instancias do objeto, após declarado __str__ 
# para saber como foi instanciado determinado objeto, o que tem dentro da classe x no objeto y
