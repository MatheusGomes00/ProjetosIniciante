def media(vezes, vet):
    s = 0
    for i in range(vezes):
        s += vet[i]
    return s/vezes


vetor = []
n1 = int(input('Entre com o tamanho do vetor: '))
for j in range(n1):
    vetor.append(int(input('Valor: ')))
print('A média dos números é: ', (media(n1, vetor)))
