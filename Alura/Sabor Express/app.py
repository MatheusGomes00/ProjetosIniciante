import os

restaurantes = []

"""
print("Camiseta Unissex","Tamanho: P, M, G, GG","Material: 100% algodão","Cores disponíveis: Preto, Branco, Vermelho", sep ='\n')
Com o uso de várias strings com o separador ‘sep’ indicando a quebra de linha entre cada uma delas, cada string será impressa com espaçamentos e quebras de linha.
"""

def menu():
    print("""

    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    1. Cadastrar restaurante
    2. Listar restaurantes
    3. Ativar restaurante
    4. Sair""")


def finalizar_app():
    exibir_subtitulo("Finalizando o app")


def voltar_ao_menu_principal():
    input('\nPressione a tecla enter para voltar ao menu principal')
    os.system('cls')
    main()


def exibir_subtitulo(texto):
    os.system('cls')
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)


def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes\n")
    nome = input("Insira o nome do restaurante: ")
    categoria = input("Insira a categoria: ")
    novo_restaurante = {'nome': nome, 'categoria': categoria, 'ativo': False}
    restaurantes.append(novo_restaurante)
    print(f"Restaurante {nome}, cadastrado com sucesso.")
    voltar_ao_menu_principal()


def listar_restaurantes():
    exibir_subtitulo("Listando restaurantes\n")
    print(f'\n{"Nome do Restaurante".ljust(22)} | {"Categoria".ljust(20)} | {"Estado"}')
    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f"- {nome.ljust(20)} | {categoria.ljust(20)} | {ativo}\n")
    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    nome_restaurante = input("\nInsira o nome do restaurante que deseja alterar o estado: ")
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'\nO restaurante {nome_restaurante} foi ativado com sucesso.' if restaurante['ativo'] else f'\nO restaurante foi desativado com sucesso.'
            print(mensagem)
    if not restaurante_encontrado:
        print("\nRestaurante não encontrado.")

    voltar_ao_menu_principal()


def main():
        # os.system('cls')
        menu()
        try:
            opcao = int(input("Escolha uma opção: "))
            match opcao:
                case 1:
                    cadastrar_novo_restaurante()
                case 2:
                    print("Listar restaurantes")
                    listar_restaurantes()
                case 3:
                    print("Alternar estado restaurantes")
                    alternar_estado_restaurante()
                case 4:
                    finalizar_app()
                case _:
                    print("Opção Inválida!")
                    voltar_ao_menu_principal()
        except ValueError:
            print("Opção Inválida!")
            voltar_ao_menu_principal()


if __name__ == '__main__':
    main()
