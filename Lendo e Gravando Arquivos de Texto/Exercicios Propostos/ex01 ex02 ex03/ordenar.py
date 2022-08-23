def ordenar(lista) -> 'Lista ordenada':
    """
    Função para ordenar a lista de números.
    :param lista: recebe a lista de números.
    :return: retorna a lista de números ordenada.
    """
    lista_1 = []
    lista_2 = []
    lista_3 = []
    lista_4 = []
    lista_ordenada = sorted(lista)
    for i in lista_ordenada:
        if len(i) == 1:
            lista_1.append(i)
        elif len(i) == 2:
            lista_2.append(i)
        elif len(i) == 3:
            lista_3.append(i)
        elif len(i) == 4:
            lista_4.append(i)
    lista_completa = sorted(lista_1) + sorted(lista_2) + sorted(lista_3) + sorted(lista_4)
    return lista_completa
