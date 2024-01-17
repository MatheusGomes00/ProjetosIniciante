from livraria_2 import Livro


livro_1 = Livro('Alice in Wonderland', 'Zé Pequeno', 1884)
livro_2 = Livro('Star Wars', 'Andor', 1964)
livro_3 = Livro('Star Wars 2', 'Andor', 1964)



def main():
    # livro_2.emprestar()
    Livro.verificar_disponibilidade(1964)
    print(livro_1)


if __name__ == '__main__':
    main()
