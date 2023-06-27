pratos = ('pato_recheado', 'vinagrete', 'lasanha', 'pernil_assado', 'feijoada')
for prato in pratos:
    print(prato)
# pratos[0] = 'macarronada'  >>> irá retornar erro, pois a tupla é imutável
print(pratos[0])
# podemos apenas atribuir um novo valor para a variável, desta forma:
pratos = ('hamburger', 'pizza', 'churrasco', 'tapioca', 'cerveja_artesanal')
print(pratos[0])
print('sorvete' not in pratos)
