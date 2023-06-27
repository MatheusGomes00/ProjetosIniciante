# [].append adiciona um item a lista
lista = []
lista.append(69)
print(lista)

# [].clear limpa a lista
lista2 = [1, 3, 5, 7, 9]
lista2.clear()
print(lista2)

# [].copy copia a lista em uma nova variável...
lista3 = [3, 'python', 22, [6, 3, 9]]
l3 = lista3.copy()
print(lista3)
print(id(l3), id(lista3))
l3[0] = 59
print(lista3)
print(l3)

# [].count  faz a contagem de determinado parâmetro passado
cores = ['vermelho', 'amarelo', 'verde', 'vermelho', 'verde']
print(cores.count('vermelho'))
print(cores.count('amarelo'))
print(cores.count('verde'))

# [].extend adiciona como o append, porém vários itens de uma vez
linguagens = ['java', 'python', '.net']
print(linguagens)
linguagens.extend(['js', 'ruby', 'rest'])
print(linguagens)

# [].index retorna a primeira ocorrência de iterável, se houver item repetido, será retornado a primeira ocorrência
linguas = ['java', 'python', '.net', 'js', 'ruby', 'rest']
print(linguas.index('java'))
print(linguas.index('js'))

# [].pop conceito de pilha, e remoção da lista, sempre será removido o último item adicionado, pode ser passado o índice ou não
linguagens = ['java', 'python', '.net', 'js', 'ruby', 'rest']
linguagens.pop()
print(linguagens)
linguagens.pop()
print(linguagens)
linguagens.pop(0)
print(linguagens)

# [].remove outra forma de remover da lista determinado item, sempre a primeira ocorrência passando o objeto em si, se houver mais de um objeto se repetindo, necessário fazer incremento
carros = ['corvette', 'fordGT', 'gtr', 'skyline', 'bugati']
print(carros)
carros.remove('gtr')
print(carros)

# [].reverse inverte a lista ao contrario
comidas = ['banana', 'sorvete', 'açaí', 'churrasco', 'lasanha']
comidas.reverse()
print(comidas)
