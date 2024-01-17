class ContaBancaria:
    def __init__(self, titular='', saldo=0):
        self._titular = titular.title()
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'Titular: {self._titular.ljust(20)} | Saldo: R${self._saldo} | Conta: {self.ativo}'
    
    @property
    def ativo(self):
        return 'Ativada' if self._ativo else 'Desativada'

    def alternar_status(self):
        self._ativo = not self._ativo

    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo


conta_1 = ContaBancaria('Matheus Gomes', 500)
conta_2 = ContaBancaria('pedro euzébio', 350)
print(conta_1.titular)

print(conta_2.ativo)

print(conta_2)

ContaBancaria.alternar_status(conta_1)

print(conta_1)

