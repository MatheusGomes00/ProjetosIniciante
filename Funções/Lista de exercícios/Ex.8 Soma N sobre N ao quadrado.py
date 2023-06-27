def verifica(numb):
    j = 2
    soma = 1
    for i in range(num - 1):
        soma = soma + (j / (j ** 2))
        j += 1
    return f'{soma:.2f}'


num = int(input('Entre com o número: '))
print(verifica(num))
