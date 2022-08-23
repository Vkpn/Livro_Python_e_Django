import pickle
from pprint import pprint


def ler_configuracao() -> None:
    arquivo = open('config.dat', 'rb')
    dados = pickle.load(arquivo)
    arquivo.close()
    pprint(dados)
