# É possível passar nenhum ou vários parâmetros para uma função, tornando eles
# obrigatórios ou opcionais, para os opcionais, ao declarar o parâmetro podemos
# omitir atribuindo 'None' a ele. Os obrigatórios são apenas definidos como 'nome' abaixo.
def dados(nome, idade=None):
    if idade is not None:
        return print(f"Nome: {nome} \nIdade: {idade}")
    else:
        return print(f"Nome: {nome} \nIdade: não informada")


dados("João", 55)
