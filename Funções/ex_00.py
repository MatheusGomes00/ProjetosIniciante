def divisao(x, y):
    div = x/y
    return div


def velocidade_media(distancia, tempo):
    velocidade = divisao(distancia, tempo)
    return velocidade


def verificar():
    for i in range(4):
        dist = int(input("Entre com a distância: "))
        temp = int(input("Entre com o tempo: "))
        print(f"Velocidade média: {velocidade_media(dist, temp):.2f}")


# verificar()
