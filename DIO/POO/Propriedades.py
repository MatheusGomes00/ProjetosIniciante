"""
Propriedades gerenciadas ou propriedades computadas, trata
um método como um atributo, para isso usamos o decorador,
escrito por um @ e o seu nome. Transforma o método em uma 
propriedade. Recebe uma ação para montar o valor de uma 
variável.
"""
class Teste:
    def __init__(self, x=None):
        self._x = x

    @property  # decorador, é executado antes da função/método
    def x(self):
        return self._x or 0

    @x.setter  # modifica o valor, setar um novo valor;
    def x(self, value):
        self._x += value

    @x.deleter  # deleta
    def x(self):
        self._x = 0


teste = Teste(10)
print(teste.x)
del teste.x
print(teste.x)
teste.x = 10
print(teste.x)
