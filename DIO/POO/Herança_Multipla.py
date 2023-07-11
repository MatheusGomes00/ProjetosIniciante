class Animal:
    def __init__(self, nro_patas, ):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        # método utilizada para retornar o objeto renomeado como um dicionário, apresentando suas características

class FalarMixin:
    def __str__(self):
        return 'Olá mundo ou Hello world'
    # o conceito de 'Mixin' é utilizado para definir uma 
    # função específica ou um comportamento que é menos 
    # acoplado
    


class Mamifero(Animal):
    def __init__(self,  cor_pelo, **kwargs):
        self.cor_pelo = cor_pelo
        super().__init__(**kwargs)  
        # 'super().__init__' faz referência aos atributos da
        # classe mãe/pai; 
        # pode ser passado só '(**kwargs) ou 
        # (nro_patas*kwargs["nro_patas"])
        # é usado 'kwargs' porque o interpretador python não
        # consegue relacionar atributos de classes que recebem 
        # herança, por exemplo uma classe filha é
        # definida com 2 atributos, mas ela herda mais um 
        # atributo da classe mãe/pai, então quando vamos 
        # instanciar um novo objeto e definir seus 
        # atributos/características o interpretador retorna erro
        # acusando que o número de atributos passados está 
        # incorreto. 



class Ave(Animal):
    def __init__(self, cor_bico, **kwargs):
        self.cor_bico = cor_bico
        super().__init__(**kwargs)  
        # mesma observação do comentário anterior


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
# como foi declarado kwargs na definição dos atributos da classe
# quando vamos estancear um novo objeto, precisamos passar
# todos os atributos/caractecísticas formatados como kwargs ou
# como dicionário 'key_word=meaning', nomeado e não posicional
# print(gato)
ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo='preto', cor_bico='laranja')
print(Ornitorrinco.__mro__)  
# '__mro__' ordem de resolução do código
print(ornitorrinco)
