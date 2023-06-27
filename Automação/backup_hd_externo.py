import os
import shutil
import argparse


def atualizar_hd_externo(origem, destino):
    # Verifica se o diretório de destino existe, caso contrário, cria-o
    if not os.path.exists(destino):
        os.makedirs(destino)

    # Copia apenas os arquivos modificados desde a última atualização
    for root, dirs, files in os.walk(origem):
        for file in files:
            origem_path = os.path.join(root, file)
            destino_path = os.path.join(destino, file)

            # Verifica se o arquivo já existe no destino e se foi modificado
            if not os.path.exists(destino_path) or os.path.getmtime(origem_path) > os.path.getmtime(destino_path):
                # shutil.copy2(origem_path, destino_path)  # A função copy2 preserva metadados (data de modificação, permissões, etc.)
                shutil.copytree(origem, destino, dirs_exist_ok=True)

    print("Atualização concluída.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script para atualizar HD externo.")
    parser.add_argument("origem", help="C:/Users/Matheus Gomes/Desktop/área de trabalho/Economia")
    parser.add_argument("destino", help="E:/")
    args = parser.parse_args()

    atualizar_hd_externo(args.origem, args.destino)
