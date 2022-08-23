print('=' * 25)
print(str.center(' Jogo da Forca ', 25, '-'))
print('=' * 25)
resposta = str(input('Digite a palavra a ser adivinhada: ')).lower().strip()
resposta_temp = []
erros = 0
acertou = False
print(f'A palavra a ser adivinhada tem {len(resposta)} letras, você só pode errar 6x, boa sorte!')
for i in resposta:
    resposta_temp.append('*')
while erros < 6:
    letra = str(input('Digite uma letra: ')).lower().strip()
    if letra not in resposta:
        erros += 1
        print(f'{letra.upper()} não está na palavra - {erros}° erro.')
        print('-' * 25)
    else:
        for ind, letras in enumerate(resposta):
            if letra == letras:
                print(f'{letra.upper()} está na {ind + 1} posição da palavra.')
            if letra == letras:
                resposta_temp[ind] = letras
                print(''.join(resposta_temp).upper())
        print('-' * 25)
        palavra = str(input('Você sabe a palavra? Caso erre é Game Over! [S/N]: ')).upper().strip()
        if palavra in 'Nn':
            print('-' * 25)
            continue
        elif palavra in 'Ss':
            resultado = str(input('Qual a palavra? '))
            if resultado == resposta:
                acertou = True
                print('-' * 25)
                break
            else:
                acertou = False
                print('-' * 25)
                break
print('Fim de jogo!')
if acertou:
    print(f'Parabéns, você acertou! A palavra era: {resposta}')
else:
    print(f'Game Over. Tente novamente, a palavra era: {resposta.upper()}')
