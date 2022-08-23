import pickle


def ler_binario():
    arquivo = open('lista_num.bat', 'rb')
    dados = pickle.load(arquivo)
    arquivo.close()
    for i in dados:
        print(i)
