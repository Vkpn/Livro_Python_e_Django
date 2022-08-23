from random import randint
jogador1 = str(input('Qual o nome do jogador 1: ').title())
jogador2 = str(input('Qual o nome do jogador 2: ').title())

vitorias1 = 0
vitorias2 = 0

continuar = True

while continuar:
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)

    if dado1 > dado2:
        print('-=-' * 10)
        print(f'Os valores foram {dado1} para o {jogador1} e {dado2} para o {jogador2}')
        print(f'O {jogador1} venceu!')
        vitorias1 += 1
        print(f'Placar: {jogador1} {vitorias1} x {vitorias2} {jogador2}')
        print('-=-' * 10)
    elif dado2 > dado1:
        print('-=-' * 10)
        print(f'Os valores foram {dado1} para o {jogador1} e {dado2} para o {jogador2}')
        print(f'O {jogador2} venceu!')
        vitorias2 += 1
        print(f'Placar: {jogador1} {vitorias1} x {vitorias2} {jogador2}')
        print('-=-' * 10)
    elif dado1 == dado2:
        print('-=-' * 10)
        print(f'Os valores foram {dado1} para o {jogador1} e {dado2} para o {jogador2}')
        print(f'Não tivemos vencedores.')
        print(f'Placar: {jogador1} {vitorias1} x {vitorias2} {jogador2}')
        print('-=-' * 10)
    continuar = input('Deseja continuar? [S/N]: ')
    if continuar in 'Nn':
        continuar = False
if vitorias1 > vitorias2:
    print(f'Jogo encerrado, parabéns ao vencedor {jogador1}!')
elif vitorias2 > vitorias1:
    print(f'Jogo encerrado, parabéns ao vencedor {jogador2}!')
else:
    print(f'jogo encerrado, infelizmente não tivemos vencedor.')
