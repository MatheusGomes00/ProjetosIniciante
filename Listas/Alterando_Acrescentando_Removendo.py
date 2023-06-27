# Alterando n item de uma lista
frutas = ['maçã', 'pera', 'goiaba', 'melancia', 'banana']
print(frutas)
frutas[2] = 'mexerica'
print(frutas)

# Acrescentando n item na última posição em uma lista
frutas.append('goiaba')
print(frutas)
# Acrescentando n item em qualquer posição em uma lista
frutas.insert(0, 'manga')
print(frutas)

# Removendo n item de uma lista de forma permanente
del frutas[5]
print(frutas)
# Removendo n item de uma lista e gerando uma cópia manipulável
fruta_removida = frutas.pop(3)  # se não for passado índice remove o último item da lista
print(frutas, '\n', fruta_removida)
# Removendo n item de uma lista pelo identificador ou seu valor, nome do item
# este método remove somente a primeira ocorrência do item
frutas.remove('manga')
print(frutas)

convidados = ['Batman', 'WonderWoman', 'Flash', 'Coringa', 'Lanterna Verde']
for convidado in convidados:
    print('Welcome, ', convidado, ', feel free!')

convidados2 = ['Batman', 'WonderWoman', 'Batman', 'Flash', 'Coringa', 'Batman', 'Lanterna Verde', 'Batman']
for convidado in convidados2:
    if convidado == 'Batman':
        convidados2.remove('Batman')
    print(convidados2)
print('\n', convidados2)

# É NECESSÁRIO COPIAR LISTAS DESTA FORMA,
# SE NÃO CRIAMOS 2 VARIÁVEIS APONTANDO O MESMO VALOR
convidados3 = convidados2[:]
convidados2.append('Aquamen')
convidados3.append('MulherGavião')
print(convidados2)
print(convidados3)
foods = ['batata_frita', 'lanchão_podrão', 'pinza']
friends_foods = foods[:]

