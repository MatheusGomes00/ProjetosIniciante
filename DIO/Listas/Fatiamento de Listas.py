lista = ['p', 'y', 't', 'h', 'o', 'n']
# para localizar e 'manipular' os dados desta lista, temos 3 parâmetros, start, stop e step, sendo início, parada e passo.
print(lista[2:])  # retorna da posição 2 ao final
print(lista[:2])  # retorna do início ao ponto de parada (2 - 1)
print(lista[1:3])  # retorna do início até a parada declarada
print(lista[0:3:2])  # retorna o que for relativo ao início, parada e o passo
print(lista[::])  # retorna exatamente a mesma lista por não ter sido passado parâmetros
print(lista[::-1])  # retorna a lista de trás para frente, espelhar
