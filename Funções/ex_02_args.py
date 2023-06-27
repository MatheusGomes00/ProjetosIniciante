""" O '*args' é utilizado quando não sabemos de antemão quantos argumentos
    queremos passar para uma função. O asterisco (*) executa um empacotamento
    dos dados para facilitar a passagem de parâmetros, e a função que recebe esta
    categoria de parâmetro consegue fazer o desempacotamento. Então o '*args'
    recebe múltiplos parâmetros, desse modo, podemos passar listas e tuplas"""


def teste(arg, *args):
    print("primeiro argumento normal: {}".format(arg))
    for arg in args:
        print("outro argumento: {}".format(arg))


teste("python", "é", "muito", "legal")
""" Então o '*args' recebe múltiplos parâmetros, desse modo, podemos passar listas e tuplas"""
lista = ["é", "muito", "zica do pantano"]
teste("python", *lista)
tupla = ("é", "a linguagem", "que escolhi", "para aprender")
teste("python", *tupla)


def somar_sequencia(*args):
    soma = 0
    for arg in args:
        soma += arg
    return print(soma)


lista = [3, 9, 8, 5, 4, 7, 10]
somar_sequencia(*lista)
tupla = (80, 90, 70, 30, 50)
somar_sequencia(*tupla)
