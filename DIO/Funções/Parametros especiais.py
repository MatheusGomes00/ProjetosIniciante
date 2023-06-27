# conseguimos declarar funções somente por posição ou por keyword
# usamos a barra quando queremos que os argumentos sejam passados somente por posição
# usamos o asterisco quando queremos que os argumentos sejam passados como keywords
def criar_carro(modelo, ano, placa, /, marca, *, motor, combustivel):
    # o que está antes da barra tem de ser passado somente por posição, chave e valor não é aceito, somente posição
    # o que está depois da barra pode ser passado por posição ou keyword
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABCD-123", marca="FIAT", motor="1.0", combustivel="Gasolina")
# criar_carro(modelo="Palio", ano=1999, placa="ABCD-123", marca="FIAT", motor="1.0", combustivel="Gasolina")   # inválido

