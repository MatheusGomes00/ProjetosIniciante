def tabuada(x):
    if 1 <= x <= 9:  # modo simplificado de escrever 'if x >=1 and x <= 9'
        for i in range(10):
            print(i+1, ' x ', x, ' = ', (i+1)*x)
        s = str(f"Tabuada do {x}")
        return s
    else:
        s = str(f"O valor {x} não está entre 1 e 9.\nTente novamente.")
        return s


def imc(p, h):
    if p and h == 0:
        s = str('Valor inválido!')
    else:
        s = p/(h*h)
    return s


def fatorial(num):
    j, r = 1, 1
    for i in range(num):
        r *= j
        j += 1
    return r


while True:
    print('Menu:\n1-Tabuada\n2-IMC\n3-Fatorial\n4-Sair')
    opt = int(input('Opção: '))
    if opt == 1:
        n1 = int(input('Tabuada \nEntre com um valor: '))
        print(tabuada(n1))
    elif opt == 2:
        peso = float(input('IMC\nPeso: '))
        altura = float(input('Altura: '))
        print('IMC: ', imc(peso, altura))
    elif opt == 3:
        fator = int(input('Fatorial\nEntre com um valor: '))
        print(f'Fatorial de {fator} = ', fatorial(fator))
    elif opt == 4:
        print('Sair')
        break
    else:
        print('Opção inválida')
