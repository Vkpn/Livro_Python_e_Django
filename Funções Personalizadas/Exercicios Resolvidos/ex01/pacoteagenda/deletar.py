def excluir(agenda):
    """
    Função para excluir um contato da agenda.
    :param agenda: recebe a agenda para imprimir as opções disponíveis.
    :return: retorna o índice do contato a ser deletado.
    """
    for index, p in enumerate(agenda):
        print(f'{index + 1}° - {p[0].title()} = {p[1]} ')
    deletar = int(input('Qual índice do contato a ser deletado? '))
    return deletar - 1
