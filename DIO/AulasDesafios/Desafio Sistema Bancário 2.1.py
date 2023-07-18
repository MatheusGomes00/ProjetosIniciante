from abc import ABC, abstractmethod
import datetime, textwrap

class Conta:
    def __init__(self, numero, cliente):
        self.saldo = 0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = Cliente
        self.historico = Historico()

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self.cliente
    
    @property
    def historico(self):
        return self.historico
    
    @classmethod
    def nova_conta(cliente, numero):
        return Conta(numero, cliente)

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n*** Operação falhou! Você não tem saldo \
                  suficiente. ***")
            
        elif valor > 0:
            self._saldo -= valor
            print("\n*** Saque realizado com sucesso! ***")
            return True
        
        else:
            print("\n*** Operação falhou! O valor informado \
                  é inválido. ***")
            
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n*** Depósito realizado com sucesso! \
                  ***")
        else:
            print("\n*** Operação falhou! O valor informado \
                  é invalido. ***")
            return False
        
        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, 
                 limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saque = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.
             transacoes if transacao["tipo"] == Saque.
             __name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n*** Operação falhou! O valor do saque \
                  excede o limite. ***")
            
        elif excedeu_saques:
            print("\*** Operação falhou! Número máximo \
                  de saques excedido. ***")
            
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """
    

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime
                ("%d-%m-%Y %H:%M:%s")
            }
        )


class Transacao(ABC):    
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registar(self, conta):
        self.conta = Conta
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento



def menu():
    menu = '''\n
    =======MENU=======
    [D]\t-Depositar
    [S]\t-Sacar
    [E]\t-Extrato
    [NC]\t-Nova conta
    [LC]\t-Listar contas
    [NU]\t-Novo usuário
    [Q]\t-Sair
    '''
    return input.upper((textwrap.dedent(menu)))


# Função depositar
def depositar(dep, ext, sld):
    if dep > 0:  # caso o depósito seja maior que zero
        sld += dep  # adiciona o valor do deposito no saldo da conta
        ext = ext + f'Depósito de: R${dep:.2f}\n'  # registra no extrato a operação realizada
        print(f'\nDepósito de R${dep:.2f} realizado!')
    else:  # se o valor não for maior que zero retorna erro
        print(f'\nValor de depósito incompatível!\nReinicie a operação.')
    return ext, sld  # retorna o valor atualizado para as variáveis extrato e saldo


# Função sacar
def sacar(*, saque1, saldo1, n_saques1, extrato1, limite1, lim_saque1):
    if 0 < saque1 <= saldo1 and saque1 <= limite1:  # verifica se o saque é maior igual que zero e menor igual ao saldo
        if n_saques1 <= lim_saque1:  # verifica se o número de saques do dia é menor que o limite por dia
            saldo1 -= saque1  # subtrai o valor do saque no total do saldo
            print('\nOperação realizada com sucesso.\nRetire o valor na boca do caixa!')
            extrato1 = extrato1 + f'Saque de: R${saque1:.2f}\n'  # registra no extrato a operação realizada
            n_saques1 += 1  # adiciona 1 no número total de saques realizados no dia
        else:  # verifica se excedeu o limite de saques, encerra e reinicia o processo
            print('\nLimite de 3 saques excedido!\nOperação cancelada.')
    elif saque1 > limite1:  # verifica se o valor do saque é maior que o limite em conta disponível
        print('\nValor indisponível\nPermitido somente R$500,00 por saque.')
    else:  # verifica se o valor do saque é maior que o saldo ou menor igual a zero
        print('\nNão é possível sacar esta quantia!')
    return saldo1, extrato1, n_saques1


def extract(saldo, *, extrato2):
    mostra = f'\n========================' \
             f'\n         Saldo: {saldo}\n\n' \
             f'== == == == == == == == == =='\
             f'\n         {extrato2}'\
             f'\n========================'
    return mostra


def criar_user(users):
    cad_cpf = int(input('\nDigite o CPF (somente números): '))
    validacao = filtro_user(cad_cpf, users)
    if validacao:
        print('\n== Usuário já cadastrado! ==')
        return
    else:
        nome = input('\nDigite o nome do novo usuário: ')
        data_nascimento = input('\nDigite a data de nascimento (dd-mm-ano): ')
        endereco = input('\nDigite o endereço (logradouro, nro - bairro - cidade/sigla estado): ')
        users.append({'cpf': cad_cpf, 'nome': nome, 'data_nascimento': data_nascimento, 'endereco': endereco})
        print('\nNovo usuário cadastrado com sucesso!')
        return users


def filtro_user(cad_cpf, users):
    for user in users:
        if user['cpf'] == cad_cpf:
            return user
    return


def criar_conta(numero_conta, agencia, users):
    if not users:
        teste = input('\nNão existem usuários criados para vincular conta.\n\nDeseja cadastrar novo usuário? S/N ').upper()
        if teste == 'S':
            criar_user(users)
            return
    else:
        cad_cpf = int(input('\nDigite o CPF (somente números): '))
        user = filtro_user(cad_cpf, users)
        if user:
            print('\nConta cadastrada com sucesso!')
            return {'agencia': agencia, 'num_conta': numero_conta, 'usuário': user}
        else:
            print('\nUsuário não localizado, operação encerrada.')
            return


def listar_contas(contas):
    if contas:
        for conta in contas:
            print(f'''
                Agência:    {conta['agencia']}
                C/C:          {conta['num_conta']}
                Titular:      {conta['usuário']['nome']}
            ''')
    else:
        return


def main():
    clientes = []
    contas = []
    while True:  
        option = menu
        if option == 'D':  
            depositar(clientes)

        elif option == 'S':  
            sacar(clientes)

        elif option == 'E': 
            exibir_extrato(clientes)
        
        elif option == 'NU':
            criar_cliente(clientes)

        elif option == 'NC':
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif option == 'LC':
            listar_contas(contas)

        elif option == 'Q': 
            break  
        
        else:
            print('\n\nOpção inválida, digite novamente.')


main()



