import json


def titulo():
    print("****************")
    print("****Dicionário****")
    print("****************")


def key_words():  # retorna a palavra-chave
    # words = [input("Entre com a palavra-chave: ") for word in range(0, 5)]
    titulo()
    word = input("Entre com a palavra-chave: ")
    return word


def meaning(word):  # Significado* recebe o título e a palavra-chave
    dicionario = {}
    significado = input("Entre com o significado: ")
    dicionario[word] = significado  # adiciona no dicionário a palavra-chave e seu significado
    return dicionario


def convert_remove():  # converte o dicionário em uma 'string' e remove os caracteres especiais '{}' e ' "" '
    dicionario_bruto = meaning(key_words())  # atribui o dicionário bruto gerado na função 'meaning()' na variável
    ''' a linha 29 converte o dicionário bruto em uma 'string' no formato json,
       o [1:-1] faz o fatiamento da string json, a partir do segundo até o penúltimo caractere,
       removendo os colchetes no início e no fim da string'''
    dicionario_convertido = json.dumps(dicionario_bruto)[1:-1]
    print(type(dicionario_convertido))
    caracteres_remover = "\""  # \" significa aspas duplas, para diferenciar e não gerar ambiguidade
    palavra_significado = dicionario_convertido.replace(caracteres_remover, "")  # substitui as aspas duplas por espaço em branco
    print(palavra_significado)


convert_remove()
