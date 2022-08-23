login_aceito = []
login_reprovado = []
motivo = []

while True:
    login = str(input('Digite seu login: '))
    numericos = 0
    letras = 0
    if login in login.title():
        if len(login) > 6:
            for letra in login:
                if letra.isnumeric():
                    numericos += 1
            if numericos >= 2:
                for letra in login:
                    if letra.isalpha():
                        letras += 1
                if letras > 3:
                    if len(login) < 10:
                        login_aceito.append(login)
                        continuar = str(input('Deseja inserir outro Login? [S/N]: ')).upper().strip()
                        if continuar[0] == 'N':
                            break
                    else:
                        print('Deve ser menor que 10 caracteres.')
                        login_reprovado.append(login)
                        motivo.append('Deve ser menor que 10 caracteres.')
                        continuar = str(input('Deseja inserir outro Login? [S/N]: ')).upper().strip()
                        if continuar[0] == 'N':
                            break
                else:
                    print('Deve conter pelo menos 3 letras.')
                    login_reprovado.append(login)
                    motivo.append('Deve conter pelo menos 3 letras.')
                    continuar = str(input('Deseja inserir outro Login? [S/N]: ')).upper().strip()
                    if continuar[0] == 'N':
                        break
            else:
                print('Deve conter pelo menos dois números.')
                login_reprovado.append(login)
                motivo.append('Deve conter pelo menos dois números.')
                continuar = str(input('Deseja inserir outro Login? [S/N]: ')).upper().strip()
                if continuar[0] == 'N':
                    break
        else:
            print('Deve conter mais que 6 caracteres.')
            login_reprovado.append(login)
            motivo.append('Deve conter mais que 6 caracteres.')
            continuar = str(input('Deseja inserir outro Login? [S/N]: ')).upper().strip()
            if continuar[0] == 'N':
                break
    else:
        print('Primeira letra deve ser maiúscula.')
        login_reprovado.append(login)
        motivo.append('Primeira letra deve ser maiúscula.')
        continuar = str(input('Deseja inserir outro Login? [S/N]: ')).upper().strip()
        if continuar[0] == 'N':
            break
print('==' * 30)
print(str.center(' Logins Aceitos ', 60, '-'))
print('==' * 30)
for i, log in enumerate(login_aceito):
    print(f'{i + 1} - {log} - [Ok]')
print('==' * 30)
print(str.center(' Logins Reprovados ', 60, '-'))
print('==' * 30)
for i, log in enumerate(login_reprovado):
    print(f'{i + 1} - {log} - [{motivo[i]}]')
print('==' * 30)
