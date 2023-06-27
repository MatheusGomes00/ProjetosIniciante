# *args vem uma tupla, **kargs vem um dicionário
def exibir_poema(data_extenso, *args, **kargs):  # 3 argumentos para função
    texto = '\n'.join(args)  # aqui está concatenando tudo que for considerado 'args' pulando uma linha
    # args=tupla => tudo que estiver entre parenteses separado por virgula formam uma tupla, *lista imutável
    meta_dados = '\n'.join([f'{chave.title()}: {valor}' for chave, valor in kargs.items()])
    # percorre todas as chaves e valores do dicionário passado e retorna uma lista com 'chave' : 'valor' correspondentes
    mensagem = f'{data_extenso}\n\n{texto}\n\n{meta_dados}'  # a 'data_extenso' vai retornar a primeira linha do que foi passado
    # exibe a mensagem
    print(mensagem)


exibir_poema("Segunda-Feira, 27 março 2023", "Zen of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)
