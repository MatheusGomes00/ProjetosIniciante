""" Kwargs são basicamente argumentos nomeados. """


def my_function(**kwargs):
    for key, value in kwargs.items():
        print('{0} = {1}'.format(key, value))


my_function(nome='caelum')

# Ao chamar a função podemos passar um dicionário acrescido de dois asteriscos.
dicionario = {'nome': 'joão', 'idade': 25}
my_function(**dicionario)
