class Contato:

    def __init__(self, nome: str, telefone: str) -> None:
        self.__nome = nome
        self.__telefone = telefone

    def __str__(self) -> str:
        resposta = f'Nome: {self.__nome}\nTelefone: {self.__telefone}'
        return resposta

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def telefone(self) -> str:
        return self.__telefone

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @telefone.setter
    def telefone(self, telefone: str) -> None:
        self.__telefone = telefone


class Agenda:

    def __init__(self, nome_arquivo: str) -> None:
        self.__arquivo = open(nome_arquivo, 'r+a')

    @property
    def nome_arquivo(self) -> 'Arquivo a ser gravado':
        return self.__arquivo

    @nome_arquivo.setter
    def nome_arquivo(self, nome_arquivo: str) -> None:
        self.__arquivo = open(nome_arquivo, 'r+a')

    def incluir(self, contato: Contato.nome, telefone: Contato.telefone) -> str:
        resultado = None
        if contato == '':
            print('Contato não deve ser vazio.')
        else:
            self.__arquivo.write(contato)
            self.__arquivo.write(telefone)
            self.__arquivo.close()
            resultado = contato
        return resultado

    def alterar(self, contato_substituir: str, contato_novo: str) -> None:
        resultado = None
        arquivo = self.__arquivo
        lista_contatos = arquivo.readlines()[:-1]
        for n, i in enumerate(lista_contatos):
            if contato_substituir in i:
                lista_contatos[n] = contato_novo
                resultado = contato_novo
                break
            else:
                print('Contato não encontrado.')
        arquivo.writelines(lista_contatos)
        arquivo.close()
        return resultado

    def excluir_contato(self, contato_excluir: str) -> None:
        resultado = None
        arquivo = self.__arquivo
        lista_contatos = arquivo.readlines()[:-1]
        for n, i in enumerate(lista_contatos):
            if contato_excluir in i:
                lista_contatos.pop(n)
                lista_contatos.pop(n + 1)
                resultado = contato_excluir
                break
            else:
                print('Contato não encontrado.')
        arquivo.writelines(lista_contatos)
        arquivo.close()
        return resultado


class Cadastro:

    def __init__(self):
        self.__agenda = Agenda.nome_arquivo

    @property
    def agenda(self) -> 'Nome do arquivo':
        return self.__agenda

    def incluir(self, contato: str, telefone: str, nome_agenda: str) -> None:
        resultado = None
        if contato == '' or telefone == '':
            print('Contato não pode ser vazio.')
        else:
            arquivo = open(nome_agenda.lower(), 'a+')
            arquivo.write(f'{contato}\n')
            arquivo.write(f'{telefone}\n')
            arquivo.close()
            resultado = contato
        return resultado

    def alterar(self, dado_substituir: str, dado_novo: str, nome_agenda: str) -> str:
        resultado = None
        if dado_substituir == '' or dado_novo == '':
            print('Dado não pode ser vazio.')
        else:
            dado_substituir = dado_substituir
            dado_novo = dado_novo
            arquivo = open(nome_agenda, 'r')
            lista_contatos = []
            for i in arquivo.readlines():
                lista_contatos.append(i[:-1])
            arquivo.close()
            if dado_substituir not in lista_contatos:
                print('Dado a ser substituído não encontrado.')
            else:
                for k, v in enumerate(lista_contatos):
                    if dado_substituir in v:
                        lista_contatos[k] = dado_novo
                        resultado = dado_novo
                        break
                arquivo = open(nome_agenda, 'w+')
                for i in lista_contatos:
                    arquivo.write(f'{i}\n')
                arquivo.close()
            return resultado

    def excluir(self, contato_excluir: str, nome_agenda: str) -> str:
        resultado = None
        excluir = contato_excluir
        arquivo = open(nome_agenda, 'r')
        lista_contatos = []
        if excluir == '':
            print('Contato não pode ser vazio.')
        else:
            for i in arquivo.readlines():
                lista_contatos.append(i[:-1])
            arquivo.close()
            if excluir not in lista_contatos:
                print('Contato não encontrado.')
            elif excluir.isnumeric():
                print('Fornecer o nome do contato.')
            else:
                for k, v in enumerate(lista_contatos):
                    if contato_excluir in v:
                        lista_contatos.pop(k)
                        lista_contatos.pop(k)
                        resultado = contato_excluir
                        break
                arquivo = open(nome_agenda, 'w+')
                for i in lista_contatos:
                    arquivo.write(f'{i}\n')
                arquivo.close()
            return resultado


class App:

    def __init__(self):
        self.__regras = Cadastro()
        self.__loop()

    def __menu(self) -> None:
        print(' MENU '.center(40, '='))
        print('1 - Incluir Novo Contato')
        print('2 - Alterar Contato')
        print('3 - Excluir Contato')
        print('4 - Exibir Agenda')
        print('5 - Sair')

    def __opcao(self) -> int:
        opcao = int(input('Selecione um opção: '))
        if opcao == '':
            resultado = -1
        else:
            resultado = opcao
        return resultado

    def __nome_agenda(self) -> str:
        arquivo = 'agenda_telefonica'
        resultado = arquivo
        return resultado

    def __ler_nome(self) -> str:
        nome = input('Nome: ').strip().title()
        resultado = nome
        return resultado

    def __ler_dado_alteracao(self) -> str:
        resultado = None
        dado = input('Alteração a ser feita: ')
        if dado.isalpha():
            resultado = str(dado.strip().title())
        elif dado.isnumeric():
            resultado = str(dado.strip())
        return resultado

    def __ler_dado(self) -> str:
        resultado = None
        dado = input('Dado a ser alterado: ')
        if dado.isalpha():
            resultado = str(dado.strip().title())
        elif dado.isnumeric():
            resultado = str(dado.strip())
        return resultado

    def __ler_telefone(self) -> str:
        telefone = input('Telefone: ').strip()
        resultado = telefone
        return resultado

    def __loop(self) -> None:
        nome_agenda = self.__nome_agenda()
        arquivo = open(nome_agenda, 'w+')
        arquivo.close()
        while True:
            self.__menu()
            opcao = self.__opcao()
            if opcao == 1:
                print('-' * 40)
                nome = self.__ler_nome()
                telefone = self.__ler_telefone()
                arq = nome_agenda
                if self.__regras.incluir(nome, telefone, arq) is not None:
                    print('Contato cadastrado com sucesso.')
            elif opcao == 2:
                print('-' * 40)
                dado = self.__ler_dado()
                dado_novo = self.__ler_dado_alteracao()
                if self.__regras.alterar(dado, dado_novo, nome_agenda) is not None:
                    print('Contato alterado com sucesso.')
            elif opcao == 3:
                print('-' * 40)
                contato = self.__ler_nome()
                if self.__regras.excluir(contato, nome_agenda) is not None:
                    print('Contato excluído com sucesso.')
            elif opcao == 4:
                print('-' * 40)
                arq = open(nome_agenda, 'r')
                lista_contatos = arq.readlines()
                if len(lista_contatos) == 0:
                    print('Agenda vazia.')
                else:
                    for k, v in enumerate(lista_contatos):
                        if k % 2 == 0:
                            print(f'{v[:-1]} ->', end=' ')
                        else:
                            print(v[:-1])
                arq.close()
            elif opcao == 5:
                print('-' * 40)
                print('Programa encerrado pelo usuário.')
                break
            else:
                print('Opção inválida!')


app = App()
