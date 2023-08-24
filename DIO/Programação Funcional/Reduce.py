"""
Redução significa aplicar uma função que recebe dois parâmetros, nos dois primeiros elementos de uma sênquencia,
aplicar novamente a função usando como parâmetros o resultado do primeiro par e o terceiro elemento, seguindo
assim até o final da sequência. O resultado final da redução é apenas um elemento.
A função 'reduce' é utilizada para aplicar uma função cumulativamente aos elementos de uma sequência (por
exemplo, uma lista) de modo a reduzi-los a um único valor.
COMBINAR ELEMENTOS DE UMA SEQUÊNCIA DE FORMA ITERATIVA.
"""
from functools import reduce

f = lambda x, y: x if x > y else y  # seleciona o maior elemento de uma lista, comparando elementos
result = reduce(f, [45, 12, 34, 281, 90, 1])
print(result)

numbers_list = [1, 2, 3, 4, 5]
soma = reduce(lambda x, y: x + y, numbers_list)
print(soma)

words_list = ['Já', 'trabalhou', 'sua', 'energia', 'hoje???']
phrase = reduce(lambda x, y: x + ' ' + y, words_list)
print(phrase)


