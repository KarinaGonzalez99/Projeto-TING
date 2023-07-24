from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    # Utiliza a função txt_importer para ler as linhas do arquivo de texto
    pathfiles = txt_importer(path_file)

    # Cria um dicionário com as informações nome, quantidade de linhas
    processfile = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(pathfiles),
        'linhas_do_arquivo': pathfiles,
    }

    try:
        # Busca se o arquivo já foi processado anteriormente
        instance.search(instance.items.index(processfile))
        print(f"Arquivo '{path_file}' ok.\n")

        return None

    except ValueError:
        # Caso o arquivo ainda não tenha sido processado, adiciona na fila
        instance.enqueue(processfile)
        print(processfile)


def remove(instance):
    # Verifica se a fila está vazia
    if len(instance.items) == 0:
        print('Não há elementos')
        return

    # Remove o primeiro elemento da fila
    removefile = instance.dequeue()
    print(f'Arquivo {removefile["nome_do_arquivo"]} removido com sucesso')


def file_metadata(instance, position):
    try:
        # Busca as informações do arquivo na posição solicitada
        metadatafile = instance.search(position)
        print(metadatafile)
    except IndexError:
        # Caso a posição solicitada não exista na fila, retorna um erro
        print("Posição inválida", file=sys.stderr)
