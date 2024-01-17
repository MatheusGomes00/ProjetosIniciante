class Livro:
    livros = []
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f"{self._titulo}, {self._autor}, {self._ano_publicacao}, {self.disponivel}"
    
    @property
    def disponivel(self):
        return "Disponível" if self._disponivel else "Emprestado"

    def emprestar(self):
        self._disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        print(f"Livros de {ano} disponíveis: ")
        for livro in Livro.livros:
            if livro._ano_publicacao == ano and livro._disponivel == True:
                print(livro)
