def verifica(vet, vezes):
    soma = 0
    cont = 0
    for j in range(vezes):
        if j % 2 != 0:
            soma += vet[j]
            cont += 1
    return soma/cont


vet1 = []
tamanho = int(input('Entre com o tamanho do vetor: '))
for i in range(tamanho):
    vet1.append(int(input('Valor: ')))
print('Média dos valores dos indices impares: ', verifica(vet1, tamanho))



