turma = []
notas = []

for c in range(1, 6):
    aluno = str(input(f'Digite o nome do {c} aluno: '))
    nota = float(input(f'Digite a nota do {c} aluno: '))
    if len(turma) == 0:
        turma.append(aluno)
        notas.append(nota)
    elif len(turma) > 0:
        if nota > max(notas):
            turma.insert(0, aluno)
            notas.insert(0, nota)
        elif nota < min(notas):
            turma.insert(len(turma), aluno)
            notas.insert(len(notas), nota)
        else:
            for i, n in enumerate(notas):
                if nota > notas[i]:
                    notas.insert(i, nota)
                    turma.insert(i, aluno)
                    break
for i, a in enumerate(turma):
    print(f'O aluno {a} tirou: {notas[i]}')
print(f'A media geral da turma foi: {sum(notas) / len(notas)}')