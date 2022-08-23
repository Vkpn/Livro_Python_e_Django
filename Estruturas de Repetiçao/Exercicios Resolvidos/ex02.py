cont = 0
for n in range(1000, 5001):
    if n % 5 == 0 and n % 3 == 0:
        print(f'{n} é divisível por 5 e 3 simultaneamente.')
        cont += 1

print(f'No intervalo enter 1000 e 5000 temos {cont} números divisíveis por 5 e 3 simultaneamente.')
