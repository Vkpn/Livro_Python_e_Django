def listar(agenda):
    """
    Função para listar os dados já salvos na agenda.
    :param agenda: recebe o parâmetro agenda de modo a imprimir os dados já salvos.
    :return: não possui retorno.
    """
    for index, p in enumerate(agenda):
        print(f'{index + 1}° - {p[0].title()} = {p[1]} ')
