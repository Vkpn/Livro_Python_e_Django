from random import randint
sorteado = randint(1, 100)
num = int(input('Digite para apostar no seu numero da sorte: '))

if sorteado == num:
    print('Você venceu!')
else:
    print('A banca sempre ganha!')

