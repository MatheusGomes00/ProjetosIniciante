# texto = input('Digite o texto: ')
# if texto == texto[::-1]:
#     print('palindromo')
# else:
#     print('não é palindromo')
    

flag1 = False  # Variável para entrada e saída do loop de verificação
k = -1  # Variável para fazer a contagem inversa do vetor crescente
texto = input('Entre com a palavra, frase ou número: ')  # Entrada de dados
if len(texto) == 1:  # Verificação se o que foi digitado possui mais de 1 dígito
    print('Digite uma palavra, frase ou número!')
else:  # Se foi digitado mais de um dígito continua
    for i in range(len(texto)):  # Loop condicional para percorrer todos os caracteres do que foi digitado
        if texto[i] == texto[k]:  # Verificação se o primeiro e o último dígito são iguais
            flag1 = False
        else:  # Caso o dígito não seja igual ao correspondente atribui "True" na variável 'flag1'
            flag1 = True
        k -= 1  # Acrescenta na contagem decrescente
    if flag1 is True:  # Caso a variável 'flag1' for "True" retorna mensagem de negação
            print('Não é palíndromo.')
    if flag1 is False:  # Caso a variável flag1 for "False" retorna mensagem afirmativa.
        print('Palíndromo!')

