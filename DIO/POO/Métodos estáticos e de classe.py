"""
Métodos de classe estão ligados à classe e não ao objeto. Eles
têm acesso ao estado da classe, pois recebem um argumento que
aponta para a classe e não para a instância do objeto. Ao 
instanciar um objeto, ao invés de ele apontar diretamente
para a instância, ele aponta para classe. E por conveção
é usado cls ao invés de self, ao declarar uma instância.

Caso seja necessário ter acesso ao contexto ou instancia da 
classe, usamos o decorador método de classe @classmethod.

Um método de classe recebe um primeiro parâmetro que aponta
para a classe, enquanto um método estático não.

Um método estático não recebe um primeiro argumento explicito.
Então pode receber nenhum argumento ou 'N' argumentos.
Ele também é um método vinculado à classe e não ao objeto da 
classe. Este método não pode acessar ou modificar o estado da
classe. Ele está presente em uma classe porque faz sentido que
o método esteja presente na classe. Ele não recebe argumento 
para apontar para uma referência (classe/instância), recebe 
apenas valores. 

Caso não seja necessário contexto da classe 
nem de uma  instância da  classe usamos um método estático 
@staticmethod.

Um método de classe pode acessar ou modificar o estado da 
classe enquanto um método estático não pode acessá-lo ou 
modifica-lo, por que ele não aponta para instância ou a classe, 
ele não tem essa referência para fazer essa modificação.

Geralmente usamos método de classe para criar métodos de 
fábrica, que são métodos que retornam uma nova instância da
classe. Ex.: uma classe pessoa que tem um método de fábrica
vai retornar uma nova instância da classe pessoa.
Geralmente usamos métodos estáticos para criar funções 
utilitárias. Ex.: em uma classe pessoa, queremos criar uma
função que valide a idade da pessoa. Alguma funcionalidade que
retorno de envolve valores.

Preciso ter acesso ao contexto da classe? Então é um método
de classe.
Não preciso de contexto nem da classe nem da instância, então
usamos método estático.

"""


class Pessoa:
    def __init__(self, nome=None, idade=None):
    # é colocado none, para não retornar erro caso não exista
        self.nome = nome
        self.idade = idade

    @classmethod  # decorador
    def criar_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2023 - ano
        return Pessoa(nome, idade)  # cls == Pessoa
        # return cls(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18


p1 = Pessoa("Matheus", 25)
# print(p) assim é retornado apenas o valor do objeto
print(p1.nome, p1.idade)  # assim retornamos o valor do atributo


p2 = Pessoa.criar_data_nascimento(1997, 9, 17, "Matheus")
print(Pessoa.e_maior_idade(18))  # retorna True/False
print(Pessoa.e_maior_idade(10))  # retorna True/False
