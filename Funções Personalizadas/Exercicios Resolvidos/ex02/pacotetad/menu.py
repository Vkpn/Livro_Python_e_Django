def menu():
    """
    Função que imprime o menu de opções.
    :return: retorna a opção selecionada pelo usuário no menu.
    """
    print('~' * 50)
    print(' Menu '.center(50, '-'))
    print('~' * 50)
    print('1 - Incluir elemento no topo da pilha')
    print('2 - Remover o elemento do topo da pilha')
    print('3 - Retorna se a pilha está vazia ou não')
    print('4 - Retorna uma lista com os itens da pilha')
    print('5 - Retorna a quantidade de elementos da pilha')
    print('6 - Sair')
    print('~' * 50)
    opc = int(input('Qual opção deseja realizar: '))
    return opc
