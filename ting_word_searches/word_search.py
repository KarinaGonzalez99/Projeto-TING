def exists_word(word, instance):
    resultadoword = []  

    # Iterando sobre cada arquivo na fila
    for index in range(len(instance)):
        searchs = instance.search(index)
        namearquivo = searchs["nome_do_arquivo"]
        linearquivo = searchs["linhas_do_arquivo"]

        resultadofor = []
        # Iterando sobre cada linha do arquivo
        for linhaum, line in enumerate(linearquivo, start=1):
            # Verificando se a palavra buscada existe na linha
            if word.lower() in line.lower():
                resultadofor.append({"linha": linhaum})

        # Se houve ocorrências da palavra no arquivo, add as informações
        if resultadofor:
            saidas = {
                "palavra": word,
                "arquivo": namearquivo,
                "ocorrencias": resultadofor,
            }
            resultadoword.append(saidas)

    return resultadoword


def search_by_word(word, instance):
    resultadoword = []

    # Iterando sobre cada arquivo na fila
    for index in range(len(instance)):
        searchs = instance.search(index)
        namearquivo = searchs["nome_do_arquivo"]
        linearquivo = searchs["linhas_do_arquivo"]

        resultadofor = []
        # Iterando sobre cada linha do arquivo
        for linhaum, line in enumerate(linearquivo, start=1):
            if word.lower() in line.lower():
                line_info = {"linha": linhaum, "conteudo": line.strip()}
                resultadofor.append(line_info)

        # Se houve ocorrências da palavra no arquivo, add as informações
        if resultadofor:
            saidas = {
                "palavra": word,
                "arquivo": namearquivo,
                "ocorrencias": resultadofor,
            }
            resultadoword.append(saidas)

    return resultadoword
