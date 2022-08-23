def menu():
    print('Selecione uma opção: '.center(40, '-'))
    print('1: Consultar a Fila Atual.')
    print('2: Incluir Alguém na Fila.')
    print('3: Atender o Próximo Cliente.')
    print('4: Sair')
    print('-' * 40)
    opc = int(input('Qual operação deseja realizar? ').strip())
    return opc
