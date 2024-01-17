class ClienteBanco:
    contas = []
    n_conta = 0
    def __init__(self, nome='', cpf='', endereco='', telefone='', email=''):
        self._nome = nome
        self._cpf = cpf
        self._endereco = endereco
        self._telefone = telefone
        self._email = email
        self._agencia = '0001'
        self._conta = ClienteBanco.n_conta + 1
        self._ativo = False
        ClienteBanco.n_conta += 1
        ClienteBanco.contas.append(self)

    def __str__(self):
        return f'Titular: {self._nome.ljust(20)} | Agência: {self._agencia} | Conta: {self._conta} | Status: {self.ativo}'
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def conta(self):
        return self._conta

    @property
    def ativo(self):
        return 'Ativada' if self._ativo else 'Desativada' 
    
    @property
    def nome(self):
        return self._nome
        
    @property
    def cpf(self):
        return self._cpf
        
    @property
    def endereco(self):
        return self._endereco
        
    @property
    def telefone(self):
        return self._telefone
        
    @property
    def email(self):
        return self._email

    def alterar_status(self):
        self._ativo = not self._ativo

    @classmethod
    def listar_contas(cls):
        for conta in cls.contas:
            print(conta)


cliente_1 = ClienteBanco('teste1', 12345, 'teste1', 'teste1', 'teste1')
cliente_2 = ClienteBanco('teste2', 12346, 'teste2', 'teste2', 'teste2')
cliente_3 = ClienteBanco('teste3', 12347, 'teste3', 'teste3', 'teste3')
ClienteBanco.listar_contas()
cliente_1.alterar_status()
ClienteBanco.listar_contas()
