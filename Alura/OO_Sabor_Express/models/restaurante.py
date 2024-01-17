from models.avaliation import Avaliation

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliation = []
        Restaurante.restaurantes.append(self)

    def __str__(self) -> str:
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}")
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliation).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '☑ Ativado' if self._ativo else '☒ Desativado'

    def alternar_status(self):
        self._ativo = not self._ativo

    def receber_avaliation(self, cliente, nota):
        if 0 < nota <= 5:
            avaliation = Avaliation(cliente, nota)
            self._avaliation.append(avaliation)

    @property
    def media_avaliation(self):
        if not self._avaliation:
            return "-"
        soma_notas = sum(avaliation._nota for avaliation in self._avaliation)
        quantidade_notas = len(self._avaliation)
        media = round(soma_notas / quantidade_notas, 1)
        return media


class Cliente:
    pedidos = []
    id_pedido = 0
    def __init__(self, nome, telefone, pedido):
        self.nome = nome
        self.telefone = telefone
        self.pedido = pedido
        Cliente.pedidos.extend({self.pedido})


    def listar_pedidos():
        for pedido in Cliente.pedidos:
            print(pedido)


# matheus = Cliente('Matheus', '35-99979-4638', '1 pizza grande + 1 coca 2lt')
# pedro = Cliente('Pedro', '16-99946-3587', '1 pizza pequena + 1 fanta lata')
# Cliente.listar_pedidos()

# cantina_2R = Restaurante("cantina_2R", "churrascaria")
# minas_grill = Restaurante("minas Grill", "churrascaria")

# minas_grill.alternar_status()

# Restaurante.listar_restaurantes()
# print(minas_grill)
