# clear() = limpa o dicionário
carros = {"chevrolet": "corsa", "audi": "a3", "dodge": "viper"}
print(carros)
carros.clear()
print(carros)
# copy() = faz uma cópia
geladeira = {"banana": "amarelo", "maçã": "vermelho", "uva": "roxo"}
frutas = geladeira.copy()
print(frutas)
# fromkeys(), é usado para adicionar novas chaves em dicionários
geladeira = geladeira.fromkeys(["morango", "abacate"])
print(geladeira)
frutas = dict.fromkeys(["morango", "abacate"], "doce")
print(frutas)
# get(), usado para identificar se uma chave está inclusa em um dicionário
contatos = {"matheus.recin@outlook.com": {"nome": "Matheus", "telefone": "99979-4638"}}
# print(contatos["chave"])  # vai retornar erro de chave inexistente, devido não existir...
print(contatos.get("chave"))  # retorna 'none' caso não for encontrado
print(contatos.get("chave", {}))  # retorna {} caso não for encontrado
print(contatos.get("matheus.recin@outlook.com", {}))  # retorna o dicionário caso exista
# items(), usado para gerar uma lista de tuplas, usado para iterar itens,
# percorrer uma determinada ordem onde cada item do dicionário vira uma tupla contendo dois itens, chave/valor
print(contatos.items())
# keys(), retorna uma lista com somente as chaves do dicionário
novo_dict = {"a": 1, "s": "Arroz", "jj": "Maria"}
print(contatos.keys())
print(novo_dict.keys())
# pop(), remove uma chave do dicionário ou retorna que não foi encontrado
carros = {"ford": {"verona": 92, "focus": 2002, "kp": 2010}}
# altera = carros.pop("verona")
# assim passamos dois argumentos, onde o segundo irá ser usado caso não seja localizado a chave solicitada
altera = carros.pop("bmw", "não localizado")
print(altera)
# popitem(), remove a última ocorrência de chave, se não houver mais chave retorna key error
carros.popitem()
print(carros)
carros = {"verona": 92, "focus": 2002, "kp": 2010}
carros.popitem()
print(carros)
# setdefault() verifica se existe uma chave e valor, se existir ignora, se não existir adiciona a chave e o valor
carros = {"verona": 92, "focus": 2002, "kp": 2010}
print(carros)
carros.setdefault("corvette", 2008)
print(carros)
# update(), simplesmente atualiza o valor do dicionário, se existir a chave ele altera o valor passado
# se não existir a chave ele adiciona a chave no dicionário existente.
linguagens = {"interpretada": {"web": "js", "scripting": "python", "desktop": "java"}}
print(linguagens)
linguagens.update({"interpretada": {"web": "flutter", "scripting": "python", "desktop": "java"}})
print(linguagens)
linguagens = {"interpretada": {"web": "js", "scripting": "python", "desktop": "java"}}
linguagens.update({"compilada": {"desktop": "c"}})
print(linguagens)
# values() faz uma iteração e retorna todos os valores das chaves do dicionário
contatos = {"matheus.recin@outlook.com": {"nome": "Matheus", "telefone": "99979-4638"},
            "elzatec@hotmail.com": {"nome": "Elza", "telefone": "99928-7758"},
            "marina.gomes@gmail.com": {"nome": "Marina", "telefone": "3333-9999"}
            }
print(contatos.values())
# in() verifica se uma chave existe ou não e retorna True ou False
contatos = {"matheus.recin@outlook.com": {"nome": "Matheus", "telefone": "99979-4638"},
            "elzatec@hotmail.com": {"nome": "Elza", "telefone": "99928-7758"},
            "marina.gomes@gmail.com": {"nome": "Marina", "telefone": "3333-9999"}
            }
resultado = "matheus.recin@outlook.com" in contatos
print(resultado)
print("idade" in contatos["elzatec@hotmail.com"])
print("nome" in contatos["marina.gomes@gmail.com"])
# del() remove um valor do dicionário, passamos o objeto que queremos remover
contatos = {"matheus.recin@outlook.com": {"nome": "Matheus", "telefone": "99979-4638"},
            "elzatec@hotmail.com": {"nome": "Elza", "telefone": "99928-7758"},
            "marina.gomes@gmail.com": {"nome": "Marina", "telefone": "3333-9999"}
            }
print(contatos)
del contatos["matheus.recin@outlook.com"]["telefone"]
del contatos["marina.gomes@gmail.com"]
print(contatos)
# adicionar itens no dicionário de forma simples
dicionario1 = {'teste1': 10, 'teste2': 20, 'teste3': 30}
print(dicionario1)
dicionario1['teste4'] = 40
print(dicionario1)