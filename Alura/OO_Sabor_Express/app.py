from models.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'mexicana')
restaurante_japa = Restaurante('Japa', 'japonesa')


restaurante_japa.receber_avaliation('Pedro', 10)
restaurante_japa.receber_avaliation('Gui', 7)
restaurante_japa.receber_avaliation('Matheus', 2)



def main():
    restaurante_japa.alternar_status()
    Restaurante.listar_restaurantes()
    

if __name__ == '__main__':
    main()
