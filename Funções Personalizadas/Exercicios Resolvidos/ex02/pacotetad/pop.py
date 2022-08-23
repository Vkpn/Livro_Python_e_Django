def pop(pilha):
    """
    Função para demonstrar qual item será removido da pilha.
    :param pilha: recebe pilha para demonstração.
    :return: não possui retorno.
    """
    for k, v in enumerate(pilha):
        if k + 1 < len(pilha):
            print(v)
        else:
            print(f'{v} <- Removendo')
