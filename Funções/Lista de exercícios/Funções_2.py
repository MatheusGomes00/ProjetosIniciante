def verifica(menor, maior):
    if menor < maior:
        print('O menor número é ', menor)
    elif maior < menor:
        print('O menor número é ', maior)
    else:
        print('Os números são iguais.')


n1, n2 = int(input('Primeiro número: ')), int(input('Segundo número: '))
verifica(n1, n2)


def soma(vetor):
    s = 0
    for i in range(5):
        s += vet[i]
    return s


vet = []
for j in range(5):
    vet.append(int(input('Número: ')))
print('A soma é: ', soma(vet))
