# Podemos trabalhar com o conceito de conjuntos da matemática
# com o 'set()'. Um set é uma coleção que não possui objetos repetidos,
# usamos sets para representar conjuntos matemáticos ou
# eliminar itens duplicados de um iterável.
numeros = {1, 2, 3, 1, 4}  # set declarado entre chaves e virgulas
print(type(numeros))
print(numeros)
fruta = "abacaxi"
set(fruta)  # o set considera cada caracter um objeto e
# elimina os objetos repetidos, e não retorna na ordem
print(fruta)
carros = {"palio", "gol", "celta", "palio"}
print(carros)
# Os conjuntos não suportam indexação nem fatiamento para tratamento dos dados,
# para acessar os valores do conjunto é preciso converter ele em uma lista
carros = list(carros)
print(carros[0])
# Para percorrer os dados do set podemos usar um for sem transformar ele em uma lista
numeros = {1, 2, 3, 1, 4}
for n in numeros:
    print(n)
# Para saber o índice do objeto dentro do laço for, podemos usar a função enumerate
carros = {"palio", "gol", "celta", "palio"}
for index, carro in enumerate(carros):  # a função enumerate faz a contagem dos indices
    print(f"{index}: {carro}")
