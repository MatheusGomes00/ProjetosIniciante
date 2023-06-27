def verifica(vet, k):
    s = vet[0]
    for i in range(k):
        if vet[i] > s:
            s = vet[i]
    return s


vetor = []
tamanho = int(input('Entre com o tamanho do vetor: '))
for j in range(tamanho):
    vetor.append(int(input('Valor: ')))
print(verifica(vetor, tamanho))


