import pickle


def salvar_binario(lista) -> None:
    """
    Função para salvar os dados ordenados em um arquivo nmo formato binário.
    :param lista: recebe a lista de dados ordenados.
    :return: não retorna nada.
    """
    arquivo = open('lista_num.bat', 'w+b')
    dados = lista
    pickle.dump(dados, arquivo)
    arquivo.close()
