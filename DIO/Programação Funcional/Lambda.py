# Python possui funções anônimas, ou seja, funções sem nome que são definidas inline e podem ser atribuidas
# a variáveis.. Com isso podemos executar funções sem declarar as mesmas do jeito convêncional. O uso de 
# lambdas deve ser controlado, pois elas podem "sujar" o código. Elas são frequentemente usadas para 
# operações simples e breves, onde criar uma função regular usando a declaração 'def' seria excessivo.
# Geralmente passada como parâmetro para métodos internos como 'filter', 'map' e 'reduce'

# multiplicação de um número(x) vezes 2
a = lambda x: x * 2
print(a)
print(a(2))

# Ordenar uma lista de acordo com um critério específico:
pessoas = [('Alice', 25), ('Bob', 30), ('Carol', 22)]
pessoas.sort(key=lambda x: x[1])  
# Ordena pela idade, no caso o 'sort' ordena, e a lambda passa a condição de que seja ordenado pelo indice 1
# do item da lista que será iterado, no caso o indice 1 refere ao item 2 da tupla
print(pessoas)


# Mapear uma função para cada elemento de uma lista:
numeros = [1, 2, 3, 4, 5]
quadrados = list(map(lambda x: x**2, numeros)) # gera uma nova lista com os quadrados dos itens da 1ª lista
# O método 'list' gera uma nova lista, o método 'map' aplica uma transformação a cada elemento de uma lista
# recebe uma função (lambda x: x**2) e uma sequência (numeros)
print(numeros, '\n', quadrados)

# Filtrar elementos de uma lista com base em uma condição:
numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
# o método 'filter' identifica valores em uma lista de acordo com dois parametros, uma função e um iterável
print(pares)

