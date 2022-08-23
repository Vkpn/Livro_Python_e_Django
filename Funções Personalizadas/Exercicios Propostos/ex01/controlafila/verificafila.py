def verifica_fila(fila):
    if len(fila) == 0:
        print('A fila está vazia.')
    else:
        for index, senha in enumerate(fila):
            for k, v in fila[index].items():
                print(f'{index + 1}° = {k.title()}')
