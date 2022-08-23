from pacotetad import menu, push, pop, is_empty, get_elementos, tamanho

pilha = []

while True:
    opcao = menu.menu()
    if opcao == 1:
        adicionar = push.push()
        pilha.append(adicionar)
    elif opcao == 2:
        if len(pilha) == 0:
            print('A pilha está vazia')
        else:
            pop.pop(pilha)
            pilha.pop()
    elif opcao == 3:
        retorno = is_empty.vazio(pilha)
        print(f'Pilha vazia: {retorno}')
    elif opcao == 4:
        retorno = get_elementos.get_elementos(pilha)
        for k, v in enumerate(retorno):
            print(f'{k + 1}° - {v}')
    elif opcao == 5:
        altura = tamanho.tamanho(pilha)
        print(f'A pilha possui {altura} itens.')
    elif opcao == 6:
        break
