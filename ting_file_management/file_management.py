import os
import sys


def txt_importer(path_file):
    # Verifica se o arquivo existe
    if not os.path.isfile(path_file):
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return

    # Verifica se a extensão do arquivo é .txt
    if not path_file.endswith('.txt'):
        print("Formato inválido", file=sys.stderr)
        return

    # Se tudo estiver ok, lê o arquivo e retorna uma lista com as linhas
    with open(path_file, 'r', encoding='utf-8') as file:
        lines = file.read().split('\n')

    return lines
