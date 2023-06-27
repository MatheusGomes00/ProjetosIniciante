# como exemplo, temos uma lista com determinados dados e
# queremos gerar uma nova lista em cima desta, removendo e adicionando novos itens.
numeros = [1, 3, 4, 6, 10, 15, 13]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(numeros, '\n', pares)

# mesmo procedimento por compreensão
numeros = [1, 2, 30, 40, 35, 29]
pares = [numero for numero in numeros if numero % 2 == 0]
print(numeros, '\n', pares)

# modificando valores
numeros = [1, 2, 30, 40, 35, 29]
quadrado = []
for numero in numeros:
    quadrado.append(numero ** 2)
print(numeros, '\n', quadrado)

# mesmo procedimento por compreensão
numeros = [1, 2, 30, 40, 35, 29]
quadrado = [numero ** 2 for numero in numeros]
print(numeros, '\n', quadrado)
