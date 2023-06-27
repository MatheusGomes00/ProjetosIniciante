# o máximo é a linguagem ser intuitiva no laço 'for' é relacionado automaticamente, o contador 'carro' com cada item da lista
carros = ['gol', 'celta', 'palio']
for carro in carros:
    print(carro)

# função enumerate atribui o índice relativo à posição
motos = ['fazer', 'twister', 'falcon']
for indice, moto in enumerate(motos):  # Índice é o contador e moto é a ‘item’ de interação
    print(f'{indice}: {moto}')
