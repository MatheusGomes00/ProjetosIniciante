#  A verificação do CPF é feita pelos 2 últimos dígitos;
#  Primeiro calcula-se a soma da multiplicação dos 9 primeiros dígitos por 10, 9, 8, ... respectivamente;
#  Em seguida obtém-se o resto da divisão deste número por 11 (Resto = Soma mod 11);
#  2 condições para verificação:
#  1° Se o resto da divisão for igual a 1 ou a 0 o primeiro dígito verificador é zero;
#  2° Se não for é necessário subtrair o resto de 11 (ou seja Resto = 11 - Resto)
def veri1(cad):
    n, first, plus, rest, mult = 10, 0, 0, 0, 0
    for j in range(9):  # Loop para multiplicar e somar os 9 primeiros dígitos
        mult = cad[j] * n  # Multiplicação dos 9 primeiros dígitos, 'j' vai de 0 a 8 referente aos indices do vetor "cad"
        n -= 1  # Reduz da variável que faz a contagem regressiva de 10 até 2
        plus += mult  # Adiciona na soma a multiplicação de cada um dos 9 primeiros dígitos
    rest = plus % 11  # Atribui a variável "rest" o resto da divisão (módulo) da soma por 11
    # Verificação do resto da divisão do primeiro digito por duas condições:
    if rest == 0 or rest == 1:  # 1° condição: se o resto é igual a zero ou um
        first = 0  # Atribui zero na variável de retorno
    else:  # 2ª condição: se não for zero ou um
        rest = 11 - rest  # É descontado o resto de 11
        first = rest  # Atribui o valor do resto na variável de retorno
    return first  # Vai ser retornado zero ou outro número de 2 a 9, referente ao primeiro dígito verificador


#  Segundo calcula-se a soma da multiplicação dos 9 primeiros dígitos por 11, 10, 9, ... , 4, 3, respectivamente e do 1º dígito verificador por 2.
#  O resto é semelhante ao que foi feito anteriormente (Resto = Soma mod 11)
#  2 condições para verificação:
#  1° Se 'Resto' for igual a 1 ou a 0, então o 2º dígito verificador é 0.
#  2° Caso contrário, o 2º dígito verificador é o resultado da subtração de Resto de 11.


def veri2(cad2):
    num, soma, second, resto, multiplica, = 11, 0, 0, 0, 0
    for k in range(9):  # Loop para multiplicar e somar os 9 primeiros dígitos
        multiplica = cad2[k] * num  # Multiplicação dos 9 primeiros dígitos, 'j' vai de 0 a 8 referente aos valores dos indices do vetor "cad"
        num -= 1  # Reduz da variável que faz a contagem regressiva de 11 até 3
        soma += multiplica  # Adiciona na soma a multiplicação de cada um dos 9 primeiros dígitos
    soma += (veri1(cad2) * 2)  # Adiciona na soma o resultado do primeiro dígito verificador
    resto = soma % 11  # Atribui a variável "resto" o resultado do resto da divisão (módulo) da soma por 11
    # Verificação do resto da divisão do segundo digito por duas condições:
    if resto == 0 or resto == 1:  # 1° Condição: Se 'Resto' for igual a 1 ou a 0
        segundo = 0  # Atribui o valor zero na variável de retorno
    else:  # 2ª condição: se não for zero ou um
        resto = 11 - resto  # É descontado o resto de 11
        segundo = resto  # Atribui o valor do resto na variável de retorno
    return segundo  # É retornado 0 ou um número de 2 a 9, referente ao segundo dígito verificador


# Se for digitado mais do que dez dígitos (tem como restringir o tamanho do input?)
# Se são números e se são números positivos acima de zero (tem como restringir o input para aceitar somente números?)
# Se são letras, símbolos ou caracteres especiais
# Se foi digitado algo ou está um espaço vazio, no início, no meio ou fim


teste1 = 0
vet = []  # Gera um vetor para armazenar os dígitos do CPF
cpf = str(input('Entre com o CPF: '))  # Atribui a variável "cpf" o CPF
for i in range(len(cpf)):  # Loop para coletar os dígitos do CPF
    vet.append(int(cpf[i]))  # Acrescenta no vetor cada um dos dígitos do CPF nos indices de 0 a 9
# Validação dos dois dígitos verificadores por 2 condições:
if vet[9] == veri1(vet) and vet[10] == veri2(vet):  # Se os valores retornados das duas funções forem iguais aos dois últimos dígitos do cpf, retorna:
    print('CPF válido')
else:  # Senão, retorna:
    print('CPF inválido')
