from pprint import pprint
corrida = {}
mv = 0
numeMv = 0
correMv = ''
camp = ''
media = 0
tempos = []

for c in range(1, 7):
    corredor = str(input(f'Qual o nome do {c}° corredor: ')).strip().title()
    while True:
        if corredor in corrida:
            print('Atribua um nome diferente para esse corredor')
            corredor = str(input(f'Qual o nome do {c}° corredor: ')).strip().title()
        else:
            break
    voltas = []
    for v in range(1, 11):
        volta = float(input(f'Tempo da {v}° volta em segundos: '))
        if mv == 0:
            mv = volta
            numeMv = v
        if correMv == '':
            correMv = corredor
        voltas.append(volta)
    corrida[corredor] = voltas
print('~' * 60)
print('Placar'.center(60, ' '))
print('~' * 60)
pprint(corrida)
print('~' * 60)
for v in corrida.values():
    for i in v:
        if i < mv:
            mv = i
            numeMv = v.index(i) + 1
for c in corrida.items():
    if mv in c[1]:
        correMv = c[0]
print(f'A melhor volta da prova foi de: {correMv}')
print(f'A volta e o tempo da melhor volta foram: {numeMv}° - {mv}')
print('~' * 60)
print(' CAMPEÃO '.center(60, ' '))
print('~' * 60)
for k, v in corrida.items():
    mediaCor = sum(v) / len(v)
    if media == 0:
        media = mediaCor
        camp = k
        tempos = v.copy()
    elif mediaCor < media:
        media = mediaCor
        camp = k
        tempos = v.copy()
print(f'O campeão foi {camp} com a media de tempo {media}.')
print(f'Os tempos de {camp} foram {tempos}')

