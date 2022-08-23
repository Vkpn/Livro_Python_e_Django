opc = input('Deseja sair do sistema? [S/N] ').upper()

if opc[0] == 'S':
    print('Saindo do sistema.')
elif opc[0] == 'N':
    print('Permanecer no sistema.')
elif opc[0] != 'N' or opc != 'S':
    print('Opção inválida!')
