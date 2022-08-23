def editar(agenda):
    """
    Função para editar um contato da agenda.
    :param agenda: recebe a agenda para imprimir as opções a serem editadas.
    :return: retorna uma lista com índice do ‘item’ a ser alterado, o dado a ser alterado e a alteração.
    """
    for index, p in enumerate(agenda):
        print(f'{index + 1}° - {p[0].title()} = {p[1]} ')
    print('-' * 40)
    indice = int(input('Qual índice do contato a ser editado? '))
    print('1 - Nome\n2 - Telefone')

    edit = int(input('Qual dado a ser editado? '))
    if edit == 1:
        nome = str(input('Digite o nome para ser alterado: ')).strip().title()
        print(f'Nome alterado para {nome.strip().title()} com sucesso.')
        altnome = [indice - 1, edit - 1, nome]
        return altnome
    elif edit == 2:
        numero = str(input(f'Digite o novo numero: '))
        print(f'Numero alterado para {numero.strip()} com sucesso.')
        altnumero = [indice - 1, edit - 1, numero]
        return altnumero
