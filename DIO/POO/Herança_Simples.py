# A classe 'Veiculo é a pai, então geramos o construtor e passamos suas características e comportamentos
class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print('Ligando o motor')

    # A função abaixo chama o método especial '__str__' para mostrar as características do veículo
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


# A próxima classe 'Caminhao' é filha de 'Veículo', então queremos adicionar o comportamento 'carregado'
# para isso geramos outro construtor '__init__' e passamos o atributo, porém como ela é filha,
# temos que fazer referência ao construtor da classe pai, então usamos a palavra reservada super,
# ela vai chamar a implementação da classe pai, permitindo a interação entre as classes
class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    # a próxima função 'esta_carregado' verifica se o caminhão está carregado ou não
    def esta_carregado(self):
        print(f"{'Sim, ' if self.carregado else 'Não '}estou carregado")


moto = Motocicleta('Azul', 'CYA123', 2)
# print(moto)
# moto.ligar_motor()

carro = Carro('Prata', 'ABC123', 4)
# carro.ligar_motor()

caminhao = Caminhao('Vermelho', 'QWE345', 6, True)
# caminhao.esta_carregado()
print(caminhao)
print(carro)
print(moto)
