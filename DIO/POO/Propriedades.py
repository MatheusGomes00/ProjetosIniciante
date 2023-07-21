"""
Em Python, o conceito de propriedades computadas ou 
gerenciaveis representa uma forma de encapsulamento que permite 
controlar o acesso e a modificação de atributos de uma classe.
Em Python 3, você pode definir uma propriedade em uma classe 
usando os decoradores @property, @<atributo>.setter e 
@<atributo>.deleter. 
Decoradores são basicamente uma função embutida que modifica o 
funcionamento de outra função.

@property: Este decorador é usado para transformar um método 
em um atributo de leitura, permitindo o acesso ao valor do 
atributo, mas sem permitir modificá-lo diretamente. 
Ele é colocado acima do método que deseja expor como uma 
propriedade.

@<atributo>.setter: Este decorador é usado para transformar 
um método em um atributo de escrita, permitindo a modificação 
do valor do atributo. Ele é colocado acima de um método que 
será usado para definir o valor do atributo.

@<atributo>.deleter: Este decorador é usado para transformar 
um método em um atributo de exclusão, permitindo que você 
exclua o atributo. Ele é colocado acima de um método que será 
usado para excluir o valor do atributo.
"""
class Teste:
    def __init__(self, valor=None):
        self._numeral = valor

    @property  # decorador, é executado antes da função/método
    def propValor(self):
        return self._numeral or 0

    @propValor.setter  # modifica o valor, setar um novo valor;
    def modifica_valor(self, value):
        self._numeral += value

    @propValor.deleter  # deleta
    def deleta_valor(self):
        self._numeral = -1


teste = Teste(10)
print(teste.propValor)
del teste.deleta_valor
print(teste.propValor)
teste.modifica_valor = 10
print(teste.propValor)
