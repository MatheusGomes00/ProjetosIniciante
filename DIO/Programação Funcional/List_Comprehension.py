"""
De uma forma bem simples podemos dizer que a compreensão de listas é um recurso onde podemos gerar uma lista
através de um for inline. Comprimir listas pode ser feito usando vários for's e fazendo condições com if para
avaliar se o elemento deve ou não estar na lista gerada...
podemos iterar a list comprehension com os métodos sum, max, min...
"""
langs = ['Python', 'Java', 'Cobol', 'Rust', 'C#', 'C', 'Ruby']
result_filter = [x for x in langs if x.lower() in ['java', 'python', 'c#', 'Go']]
print(', '.join(result_filter))


result_map = [x.upper() for x in 'matheus.recin@outlook.com']
print((''.join(result_map)))

lista = [1, 2, 3, 4, 5]

somatorio = sum([x for x in lista])
print(somatorio)

maior = max([x for x in lista])
print(maior)

menor = min([x for x in lista])
print(menor)

