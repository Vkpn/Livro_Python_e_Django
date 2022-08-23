import pickle


def salvar_configuracoes(nome: str, num: str, mac: str) -> None:
    arquivo = open('config.dat', 'w+b')
    dados = {
        'nome': nome,
        'numero_serie': num,
        'endereco_mac': mac,
    }
    pickle.dump(dados, arquivo)
    arquivo.close()
