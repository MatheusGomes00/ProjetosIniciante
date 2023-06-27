"""
O conceito de encapsulamento envolve a proteção do acesso aos métodos e
atributos de determinada classe. Python usa convenção no nome do recurso
para determinar um atributo como público ou privado. Os atributos
públicos (escrito normal) podem ser acessados fora da classe,
os privados (usa-se _ antes do nome) somente na classe.
Para acessar um atributo de fora da classe, temos de criar um método para tal.
"""


class Conta:
    def __init__(self, nro_agencia, saldo=0):  # Iniciamos o construtor da classe e definimos os atributos
        self._saldo = saldo  # Definimos os saldo como privado
        self.nro_agencia = nro_agencia  # Definimos o número da agencia como publico

    def depositar(self, valor):  # criamos o método de saque que acrescenta no saldo
        self._saldo += valor

    def sacar(self, valor):  # criamos o método sacar que decrementa no saldo
        self._saldo -= valor

    def mostrar_saldo(self):  # criamos o método de acesso ao saldo, devido atributo privado
        return self._saldo


conta = Conta('001', 100)
# print(conta._saldo) -> segundo a convenção este acesso ao atributo privado está errado
print(conta.mostrar_saldo())
print(conta.nro_agencia)

