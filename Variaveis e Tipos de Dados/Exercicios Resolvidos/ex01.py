turma = ['', '', '', '', '']
notas = [0, 0, 0, 0, 0]

turma[0] = str(input('Digite o nome do primeiro aluno: '))
notas[0] = float(input('Digite a nota do primeiro aluno: '))
turma[1] = str(input('Digite o nome do segundo aluno: '))
notas[1] = float(input('Digite a nota do segundo aluno: '))
turma[2] = str(input('Digite o nome do terceiro aluno: '))
notas[2] = float(input('Digite a nota do terceiro aluno: '))
turma[3] = str(input('Digite o nome do quarto aluno: '))
notas[3] = float(input('Digite a nota do quarto aluno: '))
turma[4] = str(input('Digite o nome do quinto aluno: '))
notas[4] = float(input('Digite a nota do quinto aluno: '))

print(f'A média das notas dos alunos da sala é: {sum(notas) / len(notas)}')
