def salvar() -> 'lista de números':
    """
    Função para ler os números salvos no arquivo 'dados.txt'.
    :return: retorna os dados salvos no arquivo.
    """
    lista = []
    with open('dados.txt', 'r+') as arquivo:
        for linha in arquivo:
            lista.append(linha[:-1])
    return lista
