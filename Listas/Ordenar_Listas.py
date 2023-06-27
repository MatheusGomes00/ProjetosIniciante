""" Para ordenar a lista de forma permanente utilizamos o método sort().
    Para ordenar a lista de forma temporária apenas durante a execução usamos o método sorted().
    A lista é ordenada em ordem alfabética, crescente ou decrescente se não for passada nenhuma função.
    Para tratar a ordenação de forma específica, podemos utilizar os parâmetros 'key' e 'reverse'
    Tanto o método list.sort() quanto a função sorted() possuem um parâmetro key
    que especifica uma função a ser chamada para cada elemento da lista antes de ser realizada a comparação.
 """
cars = ['bmw', 'volvo', 'mitsubishi', 'audi', 'ferrari']
print(cars)
cars.sort()
print(cars)
cars = ['BMW', 'volvo', 'Mitsubishi', 'audi', 'ferrari']
cars.sort(key=str.lower, reverse=True)
print(cars)
numbers = [2.45, 1.35, 3.55, 2, 1, 3]
print(numbers)
numbers.sort()
print(numbers)
"""     Na lista abaixo, temos marcas de carros iniciando com letra maiúscula e somente uma
         iniciada com letra minúscula, então ao ordenar a lista a sequencia fica primeiro MAIÚSCULAS
         e depois minúsculas."""
cars = ['BMW', 'Volvo', 'mitsubishi', 'Audi', 'Ferrari']
print(cars)
print(sorted(cars))
'''     Como já mencionado a função sorted() permite usar um parâmetro 'key' então usamos ele
        para converter os caracteres todos para minúsculo ou maiúsculo antes de fazer a ordenação.'''
print(sorted(cars, key=str.upper))
numbers = [2.45, 1.35, 3.55, 2, 1, 3]
print(numbers)
print(sorted(numbers))

