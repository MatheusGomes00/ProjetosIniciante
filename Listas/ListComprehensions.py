# from math import pi

"""lista = []
for value in range(1, 11):
    lista.append(value**2)
print(lista)"""
# pares_ate_20 = [i for i in range(0, 21, 2)]
# print(pares_ate_20)

# # Solicita a entrada do usuário
# valor = input("Digite um valor: ")
# # Utiliza a entrada do usuário em uma list comprehension
# lista = [int(valor) for numero in range(5)]
# # Imprime a lista resultante
# print(lista)
#
# words = [int(input()) for word in range(0, 5)]
# print(words)


# impares_ate_20 = [x for x in range(1, 21, 2)]
# print(impares_ate_20)
#
# print('multiples de 3 até 30')
# mult_3 = [print(numero) for numero in range(3, 30, 3)]
#
# print('cubos de 1 a 10')
# cubos = [print(n**3) for n in range(1, 11)]
# print('\n')
#
# # eleva ao quadrado os elementos da lista
# squares = [value**2 for value in range(1, 11)]
# print(squares)
# quadrados = list(map(lambda x: x**2, range(10)))
# print(quadrados)
#
# """combs = []
#     for x in [1, 2, 3]:
#         for y in [3, 1, 4]:
#             if x != y:
#                 combs.append((x, y))
#     print(combs)"""
# # verifica comparação e agrupa elementos de duas listas em uma lista de tuplas
# lista = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# print(lista)
#
# # dobra os valores da lista
# lista = [-4, -2, 0, 2, 4]
# print(lista)
# lista_dobrada = [x*2 for x in lista]
# print(lista_dobrada)
#
# # selecionar somente os elementos maiores ou iguais a zero da lista
# lista_positivos = [x for x in lista if x >= 0]
# print(lista_positivos)
#
# # aplicar uma função para todos os elementos
# lista_function = [abs(x) for x in lista]  # a função abs() retorna o valor absoluto de um número para chegar a zero
# print(lista_function)
#
# # chama um método em cada elemento
# fresh_fruits = ['    banana', '    loganberry  ', '    passion fruit   ']
# fresh_fruits_2 = [x.strip() for x in fresh_fruits]
# print(fresh_fruits_2)
#
# # cria uma lista de tuplas com (numero, seu_quadrado)
# lista_tupla = [(x, x**2) for x in range(6)]  # é necessário declarar a tupla entre parenteses (x, x**2) na listcomp se não retorna erro
# print(lista_tupla)
#
# # nivela uma lista usando uma 'listcomp' com 2 laços 'for'
# vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# vec = [num for elem in vec for num in elem]
# print(vec)
#
# # cria uma lista complexa com o valor de pi arredondando até 5 casas decimais
# lista_pi = [str(round(pi, i)) for i in range(1, 6)]
# print(lista_pi)
#
#
#
#
#
