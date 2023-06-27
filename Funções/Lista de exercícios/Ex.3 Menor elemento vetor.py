def verifica(vet, vezes):
    s = vet[0]
    for i in range(vezes):
        if vet[i] < s:
            s = vet[i]
    return s


vet1 = []
repete = int(input('Entre com o tamanho do vetor: '))
for j in range(repete):
    vet1.append(int(input('Valor: ')))
print(verifica(vet1, repete))
