from pacoteagenda import menu, incluir, editar, deletar, procurar, listar

agenda = []

while True:
    opcao = menu.menu()
    if opcao == 1:
        contato = incluir.incluir()
        agenda.append(contato.copy())
        contato.clear()
    elif opcao == 2:
        alteracao = editar.editar(agenda)
        agenda[alteracao[0]][alteracao[1]] = alteracao[2]
    elif opcao == 3:
        excluir = deletar.excluir(agenda)
        agenda.pop(excluir)
    elif opcao == 4:
        procurar.procurar(agenda)
    elif opcao == 5:
        listar.listar(agenda)
    elif opcao == 6:
        break
