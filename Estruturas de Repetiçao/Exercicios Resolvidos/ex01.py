alunos = []
notas = []
soma = 0

for an in range(1, 6):
    alun = str(input(f'Digite o nome do {an}° aluno: '))
    alunos.append(alun)
    nota = float(input(f'Digite a nota do {an}° aluno: '))
    notas.append(nota)

for n in notas:
    soma += n

media = soma / len(notas)

print(f'A média da turma foi: {media:.1f}')
