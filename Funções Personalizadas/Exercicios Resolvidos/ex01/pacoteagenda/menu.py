def menu():
    """
    Função para imprimir o menu de opções.
    :return: retorna a opção selecionada.
    """
    print('~' * 40)
    print(' menu '.center(40, '-').upper())
    print('~' * 40)
    print('1 - Incluir um Contato')
    print('2 - Editar um Contato')
    print('3 - Excluir um Contato')
    print('4 - Localizar Pelo Nome')
    print('5 - Listar Telefones')
    print('6 - Sair da Agenda')
    print('~' * 40)
    opcao = int(input('Qual operação deseja realizar: '))
    return opcao
