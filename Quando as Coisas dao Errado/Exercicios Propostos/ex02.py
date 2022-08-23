try:
    arquivo = open('abcxyz.txt', 'r')
    for linha in arquivo:
        print(linha)
except IOError as erro:
    print('Arquivo abcxyz.txt não encontrado.')
    print(erro)
    raise
