"""
Propriedades gerenciadas ou propriedades computadas, pelo que eu entendi,
vai tratar um método como um atributo, para isso usamos o decorador,
escrito por um @ e o seu nome.
"""
class Teste:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = 0


teste = Teste(10)
print(teste.x)
del teste.x
print(teste.x)
teste.x = 10
print(teste.x)
