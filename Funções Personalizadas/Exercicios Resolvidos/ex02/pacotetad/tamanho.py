def tamanho(pilha):
    """
    Função para retornar o tamanho da pilha.
    :param pilha: recebe o parâmetro pilha para contagem.
    :return: retorna o tamanho da pilha.
    """
    if len(pilha) == 0:
        print('A pilha está vazia.')
    else:
        return len(pilha)
