# Um dicionário é um conjunto não-ordenado de pares chave:valor,
# onde as chaves são ÚNICAS em uma dada instância do dicionário.
# Dicionários são delimitados por chaves: {},
# e contém uma lista de pares chave:valor separado por vírgulas
# podemos declarar dicionários de duas formas:
pessoa = {"nome": "Matheus", "idade": 25}  # declaração entre chaves
print(type(pessoa))
print(pessoa)
pessoas = dict(nome='maria', idade=27)  # declaração pela função builtin 'dict'
print(type(pessoas))
# Os dados são acessados e modificados pelas chaves
pessoa['Telefone'] = '99999-3333'  # acionado nova chave 'Telefone' no dicionario 'pessoa'
print(pessoa)
jovem = {'nome': 'Matheus', 'idade': 25, 'Telefone': '35 99979-4638'}
print(jovem['nome'])
print(jovem['idade'])
print(jovem['Telefone'])
print(jovem)
# Dicionários podem armazenar qualquer tipo de objeto python como valor,
# desde que a chave para esse valor seja um objeto único imutável como (string e números)
# assim, podemos criar dicionários aninhados ou (dicionários dentro de dicionários)
contatos = {
    "matheus.recin@outlook.com": {"nome": "matheus", "telefone": "35 99979-4638" },
    "matheusgomes569@yahoo.com.br": {"nome": "matheus", "telefone": "99999-3333"},
    "elzatec72@gmail.com": {"nome": "elza", "telefone": "35 99928-7758"}
}
print(contatos["matheus.recin@outlook.com"]["telefone"])
# A forma mais comum para percorrermos os dados em um dicionário é com o for
for chave in contatos:
    print(chave, contatos[chave])
carros = {"chevrolet": "corsa", "audi": "a3", "dodge": "viper"}
for chave, valor in carros.items():
    print(chave, valor)
