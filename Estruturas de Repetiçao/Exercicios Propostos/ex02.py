contador = 0
for n in range(1000, 9001):
    if n % 2 == 0:
        if n % 4 == 0 and n % 3 == 0:
            contador += 1
print(f'Entre 1000 e 9000 temos {contador} números pares divisíveis por 4 e 3 simultaneamente.')
