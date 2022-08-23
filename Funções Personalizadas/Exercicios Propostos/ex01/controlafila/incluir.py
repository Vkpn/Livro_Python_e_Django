def incluir(fila):
    pessoa = str(input('Nome da pessoa a ser inserida na fila: ')).lower().strip()
    rg = int(input(f'RG do(a) {pessoa.title()}: '))
    cadastro = {pessoa: rg}
    print('-' * 40)
    print(f'{pessoa.title()} você está na posição: {len(fila) + 1}°')
    return cadastro
