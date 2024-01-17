class Livro:
    livros = []
    def __init__(self, titulo='', autor='', paginas=0):
        self._titulo = titulo.capitalize()
        self._autor = autor.capitalize()
        self._paginas = paginas
        Livro.livros.append(self)

    def __str__(self):
        return f'{self._titulo.ljust(20)} | {self._autor.ljust(20)} | {self._paginas} páginas'
    
    @property
    def titulo_autor(self):
        return f'{self._titulo} por {self._autor}'
    
    def aumentar_paginas(self, quantidade):
        self._paginas += quantidade

    @classmethod
    def listar_livros(cls):
        print(f'{'Título'.ljust(20)} | {'Autor'.ljust(20)} | Nº páginas')
        for livro in cls.livros:
            print(livro)
            

livro_1 = Livro('Andor', 'desconhecido', 308)
livro_2 = Livro('Tera', 'wordshinigam', 559)
livro_3 = Livro('A lenda do bardo', 'Hefrayn', 780)
Livro.listar_livros()
