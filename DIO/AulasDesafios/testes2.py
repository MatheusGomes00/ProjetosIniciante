import textwrap

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
    ==>'''
    return input(textwrap.dedent(menu)).upper()


def listar_contas(contas):
    if len(contas) == 0:
        print("*** Não existem contas criadas! ***")
    else:
        for conta in contas:
            print("=" * 80)
            print(textwrap.dedent(str(conta)))


def main():
    contas = []
    while True:
        opt = menu()
        if opt == 'LC':
            listar_contas(contas)
        else:
            break


main()
