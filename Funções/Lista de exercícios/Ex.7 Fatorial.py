def fatorial(x):
    r, j = 1, 1
    for i in range(x):
        r *= j
        j += 1
    return r


num = int(input('Entre com um valor: '))
print(f'O fatorial de {num} é: ', fatorial(num))
