class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self._nome = nome.capitalize()
        self._idade = idade
        self._profissao = profissao.upper()
        
    def __str__(self):
        return f'{self._nome}, {self._idade} anos - {self._profissao}'
    
    def aniversario(self):
        self._idade += 1
    
    @property
    def saudacao(self):
        return f'Saudações {self._nome}, bem vindo a nossa empresa!\nEsperamos que se saia bem no seu novo cargo como {self._profissao}.'


pessoa_1 = Pessoa('matheus', 26, 'técnico de suporte')

print(pessoa_1)

pessoa_1.aniversario()

print(pessoa_1.saudacao)

print(pessoa_1)
