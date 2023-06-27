def hello(meu_nome, idade):
    print(f'Olá {meu_nome}!\nSua idade é: {idade} ')


hello('Matheus', 25)
print('\n')
nome = input('Nome: ')
idade = int(input('Idade: '))
hello(nome, idade)
print('\n')


def soma(a, b):
    s = a + b
    return s


x = input('Digite o primeiro valor: ')
y = input('Digite o segundo valor: ')
resp = soma(x, y)
print(f'A soma é {resp}')
print(f'A média é {resp/2}')
