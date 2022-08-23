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
                    print('Tudo OK!')
                else:
                    print('Deve ser menor que 10 caracteres.')
            else:
                print('Deve conter pelo menos 3 letras.')
        else:
            print('Deve conter pelo menos dois números.')
    else:
        print('Deve conter mais que 6 caracteres.')
else:
    print('Primeira letra deve ser maiúscula.')


