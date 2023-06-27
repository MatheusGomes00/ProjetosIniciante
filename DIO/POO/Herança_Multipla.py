class Animal:
    def __init__(self, nro_patas, ):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class FalarMixin:
    def __str__(self):
        return 'Olá mundo ou Hello world'


class Mamifero(Animal):
    def __init__(self,  cor_pelo, **kwargs):
        self.cor_pelo = cor_pelo
        super().__init__(**kwargs)


class Ave(Animal):
    def __init__(self, cor_bico, **kwargs):
        self.cor_bico = cor_bico
        super().__init__(**kwargs)


class Ornitorrinco(Mamifero, Ave, FalarMixin):
    print(FalarMixin())
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     print(Ornitorrinco.__mro__)  # o método __mro__ vai mostrar a ordem de resolução do programa


class Gato(Mamifero):
    pass


class Leao(Mamifero):
    pass


gato = Gato(nro_patas=4, cor_pelo='caramelo')
# print(gato)
ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo='preto', cor_bico='laranja')
print(Ornitorrinco.__mro__)
print(ornitorrinco)
