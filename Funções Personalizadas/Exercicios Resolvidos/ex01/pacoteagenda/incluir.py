def incluir():
    """
    Função para incluir um contato na agenda.
    :return: Lista contendo nome e telefone
    """
    nome = str(input('Digite o nome da pessoa a ser cadastrada: ')).strip().title()
    telefone = str(input('Digite o telefone da pessoa a ser cadastrada: ')).strip()
    contato = [nome, telefone]
    return contato
