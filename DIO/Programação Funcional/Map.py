"""
A função 'map' pede dois parâmetros:
    1. Função: Será executada recebendo item a item como parâmetro. A função retorna o item modificado.
    2. Iterável que desejamos modificar.
Ao final da execução será retornada uma nova lista de objetos com os valores modificados pela função.
"""

result = list(map(lambda x: x.upper(), 'matheus.recin@outlook.com'))
print(result)

name = 'matheus da silva gomes'
# name_list = name.split()
name_capitalize = list(map(lambda x: x.capitalize(), name.split()))
print(name_capitalize)
