processos = []
print('~' * 40)
print(' Processos '.center(40, '-'))
print('~' * 40, '\n')
while True:
    print(' MENU '.center(40, '-'))
    print('1. Incluir um processo na pilha.')
    print('2. Retirar um processo da pilha.')
    print('3. Encerrar o programa.')
    print('-' * 40)
    opcao = int(input('O que deseja fazer: '))
    if opcao == 3:
        processos.clear()
        break
    elif opcao == 1:
        processo = str(input('Digite o nome do processo a ser incluído: ')).strip().title()
        processos.append(processo)
        print('-' * 40)
        for num, pro in enumerate(processos):
            print(f'{num + 1}° - {pro}')
        print('-' * 40)
    elif opcao == 2:
        if len(processos) == 0:
            print('A pilha de processos já está vazia.')
        else:
            for num, pro in enumerate(processos):
                print(f'{num + 1}° - {pro}')
            excluir = int(input('Qual processo você deseja excluir: '))
            print(f'Removido o processo N°: {excluir + 1} - {processos[excluir]}')
            processos.pop(excluir - 1)
            print('-' * 40)
            if len(processos) != 0:
                for num, pro in enumerate(processos):
                    print(f'{num + 1}° - {pro}')
                print('-' * 40)
            else:
                print('Pilha de processos vazia.')
print('-' * 40)
print('Programa encerrado com sucesso.')
