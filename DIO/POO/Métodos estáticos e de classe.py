"""
Caso seja necessário ter acesso ao contexto ou instancia da classe, usamos o decorador método de classe
@classmethod Caso não seja necessário contexto da classe nem de uma
instância da classe usamos um método estático @staticmethod
"""


class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

# decorador
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return Pessoa(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18


# p = Pessoa("Matheus", 25)
# print(p.nome, p.idade)
p = Pessoa.criar_de_data_nascimento(1997, 9, 17, "Matheus")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(10))
