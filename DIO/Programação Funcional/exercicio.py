"""
Crie um programa que receba uma lista de números inteiros. Remova todos os números ímpares maiores que trinta.
Exemplo: [1, 21, 31, 41] ... resultado [1, 21, 41].
"""
# tamanho = int(input("Entre com o tamanho da lista: "))
# lista = [int(input("Insira um valor: ")) for n in range(tamanho)]
# print(lista)
# result = [num for num in lista if num <= 30 or num % 2 == 0]
# print(result)

"""
Crie um programa que receba uma lista de números, e no final da execução retorne a mesma lista com os números 
elevados ao cubo.
"""
tamanho = int(input("Entre com o tamanho da lista: "))
lista = [int(input("Insira um valor: ")) for n in range(tamanho)]
print(lista)
f = lambda x: pow(x, 3) # x ** 3
# lista = [1, 3, 5, 7, 9]
lista = list(map(f, lista))
print(lista)
