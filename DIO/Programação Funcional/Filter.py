# Podemos aplicar uma função para filtar os valores de nossos ojetos iteráveis como: listas, tuplas e strings.
# A função filter pede dois parâmetros: 
# 1. Função: Será executada recebendo item a item como parâmetro. A função deve retornar um bool, se o retorno
# for 'False' o item será removido da lista gerada.
# 2. Iterável que desejamos filtrar.

func = lambda x: x.lower() in ['java', 'python', 'c#']
# Função que verificar se determinado 'x' passado, está na lista ['java', 'python', 'c#']
langs = ['Python', 'Java', 'Cobol', 'Lisp', 'C++', 'C#', 'Ruby']
# Geramos uma lista com o método 'list' e com o método 'filter' passamos a função 'func' e a lista 'lang'
# Para cada item da lista 'lang' a função 'func' vai converter para minúsculo e verificar se contém na
# lista ['java', 'python', 'c#']...
print(list(filter(func, langs)))

msg = list(filter(lambda x: x not in ['a', 'e', 'i', 'o', 'u'], 'Eu gosto de programar em Python'))
print(msg)
print(''.join(msg))
