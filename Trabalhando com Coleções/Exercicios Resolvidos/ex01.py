turma = {}

while True:
    aluno = str(input('Digite o nome do aluno: ')).lower().strip()
    notas = []
    for n in range(0, 3):
        nota = float(input(f'Digite a {n + 1} nota do {aluno.title()}: '))
        print(f'{n + 1} nota do {aluno.title()} inserida com sucesso! = Nota: {nota}\n-----')
        notas.append(nota)
    print(f'Aluno: {aluno.title()}\nNotas: {notas}\n[Inseridos com sucesso]\n-----')
    turma[aluno] = notas.copy()
    notas.clear()
    continuar = str(input('Deseja informar mais algum aluno? [S/N]: ')).strip().upper()
    if continuar in 'Nn':
        print('')
        break
    else:
        print('-=-' * 20)
print('~' * 55)
print(f'Boletim da Turma'.center(55, '~'))
print('~' * 55)
for k, v in turma.items():
    print(f'{k.title() + ":":<12}', end='')
    for i, n in enumerate(v):
        if i != 2:
            print(f' {n:>4.1f} |', end='')
        else:
            print(f'{n:>4.1f}\t', end='')
    media = sum(v) / len(v)
    print(f'{media:>4.1f}\t', end='')
    if media >= 7:
        print('Aprovado')
    elif media < 3:
        print('Reprovado')
    else:
        print('Prova Final')
