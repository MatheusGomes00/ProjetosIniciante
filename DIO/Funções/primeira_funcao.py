def exibir_mensagem():
    print("Olá mundo!")


def exibir_mensagem_2(nome):  # dessa forma sem atribuir valor ao 'nome' é obrigatório passar o parametro ao chamar a função
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anonimo"):
    # dessa forma ao atribuir um valor ao 'nome'
    # fica opcional passar o parâmetro ao chamar a função
    # se não for passado nada ao chamar a função, ela considera o que já está atribuído
    print(f"Welcome back {nome}!")


exibir_mensagem()
exibir_mensagem_2(nome="Matheus")
exibir_mensagem_3()
exibir_mensagem_3(nome="Mario")
