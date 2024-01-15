# Sistema bancário
# Função que retorna o menu
def menu():
    return '''
MENU
[D]-Depositar
[S]-Sacar
[E]-Extrato
[Q]-Sair
'''


# Função depositar
def depositar():
    global extrato, saldo  # define as variáveis extrato e saldo no escopo global
    deposito = float(input('Digite o valor do depósito: '))  # recebe o valor do depósito
    if deposito > 0:  # caso o depósito seja maior que zero
        saldo += deposito  # adiciona o valor do deposito no saldo da conta
        extrato = extrato + f'Depósito de: R${deposito:.2f}\n'  # registra no extrato a operação realizada
        retorno = f'Depósito de R${deposito:.2f} realizado!\nObrigado por utilizar nosso banco.'
    else:  # se o valor não for maior que zero retorna erro
        retorno = f'Valor de depósito incompatível!\nReinicie a operação.'
    return retorno
  

# Função sacar
def sacar():
    global saldo, n_saques, extrato, limite, lim_saque
    saque = float(input('Digite o valor do saque: '))
    if 0 < saque <= saldo and saque <= limite:  # verifica se o saque é maior igual que zero e menor igual ao saldo
        if n_saques <= lim_saque:  # verifica se o número de saques do dia é menor que o limite por dia
            saldo -= saque  # subtrai o valor do saque no total do saldo
            n_saques += 1  # adiciona 1 no número total de saques realizados no dia
            retorno = 'Operação realizada com sucesso.\nRetire o valor na boca do caixa!'
            extrato = extrato + f'Saque de: R${saque:.2f}\n'  # registra no extrato a operação realizada
        else:  # verifica se excedeu o limite de saques, encerra e reinicia o processo
            retorno = 'Limite de 3 saques excedido!\nOperação cancelada.'
    elif saque > limite:  # verifica se o valor do saque é maior que o limite em conta disponível
        retorno = 'Valor indisponível\nPermitido somente R$500,00 por saque.'
    else:  # verifica se o valor do saque é maior que o saldo ou menor igual a zero
        retorno = 'Não é possível sacar esta quantia!'
    return retorno


saldo = float(0.0)  # inicia a variável saldo como zerada
extrato = ''  # inicia a variável extrato sem texto algum
limite = float(500.0)  # define o limite diário de saque em 500 reais
n_saques = int(0)  # inicia variável de contagem do número de saques zerada
lim_saque = 2  # define o limite de saques em 3 vezes
while True:  # inicia um loop infinito
    operation = input(menu()).upper()  # entrada de dados da operação desejada no menu
    if operation == 'D':  # condição para operação de depósito
        print(depositar())  # chama a função depositar
    elif operation == 'S':  # condição para operação de saque
        print(sacar())  # chama a função sacar
    elif operation == 'E':  # condição para operação de saque
        print(f'Saldo: {saldo}\n{extrato}')  # chama as variáveis que armazena o saque e o extrato
    elif operation == 'Q':  # condição para saída do loop infinito
        break  # encerra o loop infinito
    else:
        print('Opção inválida, digite novamente.')
