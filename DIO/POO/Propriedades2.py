class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento

    # @property
    # def nome(self):
    #     return self.nome
    # não é necessário declarar um property para acessar 'nome'
    # pois a variável 'nome' é pública

    @property
    def idade(self):
        _ano_atual = 2022
        return _ano_atual - self._ano_nascimento


pessoa = Pessoa("Matheus", 1997)
print(f'Nome: {pessoa.nome} \tIdade: {pessoa.idade}')
