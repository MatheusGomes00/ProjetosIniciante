# Podemos trabalhar com o conceito de conjuntos matemáticos a partir de métodos para o 'set'
# É possível fazer todas as operações relacionadas aos conjuntos matemáticos
# União de 2 conjuntos:
conjunto_a = {1, 2, 3}
conjunto_b = {4, 5}
print(conjunto_a.union(conjunto_b))  # retorna conjunto_a + conjunto_b, eliminando os repetidos
# Interseção de 2 conjuntos:
conjunto_a = {0, 1, 2, 3}
conjunto_b = {1, 3}
print(conjunto_a.intersection(conjunto_b))  # retorna o que está presente nos dois conjuntos simultaneamente
# Diferença entre conjuntos:
conjunto_a = {1, 2, 3, 5}
conjunto_b = {0, 2, 4}
print(conjunto_a.difference(conjunto_b))  # retorna o que está presente no A que não está no B
print(conjunto_b.difference(conjunto_a))  # retorna o que está presente no B que não está no A
# Diferença simétrica entre conjuntos:
conjunto_a = {0, 1, 3}
conjunto_b = {1, 2, 4}
print(conjunto_a.symmetric_difference(conjunto_b))  # retorna o que NÃO está presente nos dois conjuntos
# Verifica se determinado conjunto é um subconjunto do outro
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5, 6}
print(conjunto_a.issubset(conjunto_b))  # retorna True se conjunto_a é um subconjunto do conjunto_b
print(conjunto_b.issubset(conjunto_a))  # retorna False se conjunto_b não é um subconjunto do conjunto_a
# Verifica se determinado conjunto é superconjunto de outro
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5, 6}
print(conjunto_a.issuperset(conjunto_b))  # retorna False pois o conjunto_a não é superconjunto (está 'acima') do conjunto_b
print(conjunto_b.issuperset(conjunto_a))  # retorna True pois o conjunto_b é superconjunto do conjunto_a (está 'acima')
# Verifica se os conjuntos NÃO se relacionam
conjunto_a = {0, 1, 2, 3, 4}
conjunto_b = {5, 6, 7, 8, 9}
conjunto_c = {4, 5, 10}
print(conjunto_a.isdisjoint(conjunto_b))  # retorna True pois o conjunto_a não se relaciona com o conjunto_b
print(conjunto_b.isdisjoint(conjunto_c))  # retorna False pois o conjunto_b se relaciona com o conjunto_c
# Adicionar item na coleção set:
sorteio = {59, 48, 33, 29}
sorteio.add(25)  # adiciona o 25 na coleção, mas não em ordem
sorteio.add(29)  # não será adicionado o 29 por que já existe um item igual na coleção
print(sorteio)
# Limpar coleção:
sorteio = {1, 2, 3}
print(sorteio)
sorteio.clear()
print(sorteio)
# Faz uma cópia da coleção
sorteio = {55, 39, 66}
sorteio2 = sorteio.copy()
print(id(sorteio), id(sorteio2))
# descarta o número passado
numeros = {0, 1, 2, 3, 4, 10, 12, 15, 20, 39}
numeros.discard(39)  # se for passado um número que não exista na coleção o programa só ignora
print(numeros)  # retorna a coleção de números em ordem aleatória, porém sem o 39
# descarta sempre a primeira ocorrência da coleção
numeros = {0, 1, 2, 3, 4, 10, 12, 15, 20, 39}
numeros.pop()
print(numeros)
# remove determinado item da colação que seja passado
numeros = {0, 1, 2, 3, 4, 10, 12, 15, 20, 39}
numeros.remove(39)  # se for digitado um item da coleção que não existe o programa retorna erro
print(numeros)
# faz a contagem de quantos itens possui a coleção, já eliminando os itens repetidos
numeros = {0, 1, 2, 3, 4, 10, 1, 12, 2, 15, 10, 20, 39}
print(len(numeros))  #
