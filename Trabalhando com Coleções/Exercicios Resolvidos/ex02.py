fila = []

while True:
    print('Selecione uma opção: '.center(40, '-'))
    print('1: Consultar a Fila Atual.')
    print('2: Incluir Alguém na Fila.')
    print('3: Atender o Próximo Cliente.')
    print('4: Sair')
    print('-' * 40)
    opc = int(input('Qual operação deseja realizar? ').strip())
    if opc == 1:
        print('-' * 40)
        if len(fila) == 0:
            print('A fila está vazia.')
        else:
            for index, senha in enumerate(fila):
                for k, v in fila[index].items():
                    print(f'{index + 1}° = {k.title()}')
    elif opc == 2:
        print('-' * 40)
        pessoa = str(input('Nome da pessoa a ser inserida na fila: ')).lower().strip()
        rg = int(input(f'RG do(a) {pessoa.title()}: '))
        fila.append({pessoa: rg})
        print('-' * 40)
        print(f'{pessoa.title()} você está na posição: {len(fila)}°')
    elif opc == 3:
        print('-' * 40)
        if len(fila) == 0:
            print('A fila está vazia.')
        else:
            for k, v in fila[0].items():
                print(f'Atendendo ao cliente {str(k).title()} - {v}')
            fila.pop(0)
    elif opc == 4:
        break
    else:
        print('-' * 40)
        print('Opção inválida!')
print('-' * 40)
print('Programa encerrado.')


