def atender(fila):
    if len(fila) == 0:
        print('A fila está vazia.')
    else:
        for k, v in fila[0].items():
            print(f'Atendendo ao cliente {str(k).title()} - {v}')
