dicionario = {}
word_list = ['amora', 'ameixa', 'abacate', 'goiaba', 'pera']
for word in word_list:
    if word in dicionario:
        dicionario[word] += 1
    else:
        dicionario[word] = 1
print(dicionario.items())
lista = [1, 2, 3, 4]
imposto = map(lambda x: x*2, lista)
print(list(imposto))

