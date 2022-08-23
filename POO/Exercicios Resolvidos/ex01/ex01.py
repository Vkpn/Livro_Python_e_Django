class Contato:

    def __init__(self, nome: str, telefone: str) -> None:
        self.__nome = nome
        self.__telefone = telefone

    def __str__(self) -> str:
        resultado = f'\nNome: ' + self.__nome
        resultado += f'\nFone: ' + self.__telefone
        return resultado

    @property
    def telefone(self) -> str:
        return self.__telefone

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome


class RepositorioContatos:

    def __init__(self):
        self.__repositorio_contatos = []

    @property
    def repositorio_contatos(self) -> 'Coleção que armazena os contatos':
        return self.__repositorio_contatos

    def incluir(self, contato: Contato) -> Contato:
        resultado = None
        if not contato == None:
            self.__repositorio_contatos.append(contato)
            resultado = contato
        else:
            print('Um contato deve ser fornecido.')
        return resultado

    def atualizar(self, indice: int, contato: Contato) -> None:
        resultado = None
        if contato == None:
            print('Um contato deve ser fornecido.')
        elif indice == None:
            print('Um índice deve ser fornecido.')
        elif indice < 0:
            print('Índice não deve ser negativo')
        else:
            self.__repositorio_contatos[indice] = contato
            resultado = contato
        return resultado

    def excluir_por_indice(self, indice: int) -> None:
        resultado = None
        if indice == None:
            print('Um índice para ser excluído deve ser fornecido.')
        elif indice < 0:
            print('O índice não deve ser negativo')
        else:
            resultado = self.__repositorio_contatos.pop(indice)
        return resultado

    def consultar_indice_por_nome(self, nome: str) -> int:
        resultado = -1
        indice = -1
        for i in range(0, len(self.__repositorio_contatos)):
            contato = self.__repositorio_contatos[i]
            if contato.nome == nome:
                indice = i
        if indice != -1:
            resultado = indice
        return resultado

    def existe(self, contato: Contato) -> bool:
        resultado = False
        for c in self.__repositorio_contatos:
            if c.telefone == contato.telefone:
                resultado = True
                break
        return resultado

    def vazio(self) -> bool:
        return len(self.__repositorio_contatos) == 0


class CadastroContatos:

    def __init__(self):
        self.__repositorio_contatos = RepositorioContatos()

    @property
    def repositorio_contatos(self) -> 'Coleção que armazena os contatos':
        return self.__repositorio_contatos

    def incluir(self, contato: Contato) -> Contato:
        resultado = None
        if self.__repositorio_contatos.existe(contato):
            input('Contato já cadastrado. Tecle enter...')
        else:
            resultado = self.__repositorio_contatos.incluir(contato)
        return resultado

    def alterar(self, contato: Contato) -> Contato:
        resultado = None
        if self.__repositorio_contatos.consultar_indice_por_nome(contato.nome) == -1:
            input('Contato não encontrado. Tecle enter...')
        else:
            indice = self.repositorio_contatos.consultar_indice_por_nome(contato.nome)
            resultado = self.__repositorio_contatos.atualizar(indice, contato)
        return resultado

    def excluir(self, contato: Contato) -> Contato:
        resultado = None
        if not self.__repositorio_contatos.existe(contato):
            input('Contato não encontrado. Tecle enter...')
        else:
            indice = self.__repositorio_contatos.consultar_indice_por_nome(contato.nome)
            if indice == -1:
                resultado = self.__repositorio_contatos.excluir_por_indice(indice)
        return resultado

    def consultar(self, nome: str) -> Contato:
        resultado = None
        if not self.__repositorio_contatos.existe(nome):
            print('Contrato não encontrado.')
        else:
            indice = self.__repositorio_contatos.consultar_indice_por_nome(nome)
            if indice != -1:
                resultado = self.__repositorio_contatos.excluir_por_indice(indice)
        return resultado


class ContatosApp:

    def __init__(self):
        self.__regras_negocio = CadastroContatos()
        self.__loop_principal()

    def __exibe_menu(self) -> None:
        self.__limpa_tela()
        print('\n Selecione um opção: ')
        print('\n 1. Incluir novo contato')
        print('\n 2. Alterar telefone de um contato')
        print('\n 3. Excluir um contato')
        print('\n 4. Consultar contato por nome')
        print('\n 5. Listar todos os contatos cadastrados')
        print('\n 6. Sair')
        print('\n')

    def __limpa_tela(self) -> None:
        print('\n' * 100)

    def __opcao_selecionada(self) -> int:
        opcao = input('Escolha uma opção: ')
        if opcao == '':
            resultado = -1
        else:
            resultado = int(opcao)
        return resultado

    def __ler_dados(self) -> Contato:
        self.__limpa_tela()
        telefone = input('\nTelefone: ')
        nome = input('\nNome:')
        resultado = Contato(telefone, nome)
        return resultado

    def __loop_principal(self) -> None:
        opcao = -1
        while opcao != 6:
            self.__exibe_menu()
            opcao = self.__opcao_selecionada()
            if opcao == 1:
                contato = self.__ler_dados()
                if self.__regras_negocio.incluir(contato) != None:
                    print('\nContato cadastrado com sucesso.')
            elif opcao == 2:
                contato = self.__ler_dados()
                if self.__regras_negocio.alterar(contato) != None:
                    print('\nContato alterado com sucesso')
            elif opcao == 3:
                self.__limpa_tela()
                telefone = input('\nTelefone: ')
                if self.__regras_negocio.excluir(contato) != None:
                    print('Contato excluído.')
            elif opcao == 4:
                self.__limpa_tela()
                nome = input('Digite o nome do contato para localizar: ')
                contato = self.__regras_negocio.consultar(nome)
                if contato != None:
                    print(f'Contato encontrado: \n{contato}\n')
            elif opcao == 5:
                self.__limpa_tela()
                if not self.__regras_negocio.repositorio_contatos.vazio():
                    for contato in self.__regras_negocio.repositorio_contatos.repositorio_contatos:
                        print(f'\n{contato}\n')
                else:
                    print('\nNenhum contato cadastrado.')
            else:
                print('Opção inválida.')
            if opcao != 6:
                input('Tecle enter para retornar ao menu...')


app = ContatosApp()
