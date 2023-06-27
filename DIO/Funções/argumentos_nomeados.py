def salvar_carro(marca, modelo, ano, placa):
    # salva carros no banco de dados ...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


# passados valores desta primeira forma corremos o risco de ser inseridos dados fora da ordem e o carregamento ser incorreto
salvar_carro("Fiat", "Palio", 1997, "PYIE-5623")
# independente da ordem que for passados parâmetros, o programa vai obedecer à atribuição das palavras...
salvar_carro(marca="Fiat", modelo="Toro", ano=2015, placa="ABC-5698")
# ao passar dois asteriscos e depois o dicionário, estamos alegando que vamos colocar um dicionário como parâmetro para função
# dessa forma a função considera cada chave e valor como uma referência
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
