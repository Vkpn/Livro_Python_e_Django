def procurar(agenda):
    """
    Função para procurar um dado específico na lista 'agenda'.
    :param agenda: recebe a lista agenda para efetuar a busca.
    :return: não possui retorno.
    """
    pessoa = str(input('Digite o nome da pessoa a ser encontrada na agenda: ')).strip().title()
    for index in agenda:
        if pessoa in index[0]:
            print(f'{index[0]} - {index[1]}')
        elif pessoa not in index[0]:
            print('Pessoa não encontrada.')
            