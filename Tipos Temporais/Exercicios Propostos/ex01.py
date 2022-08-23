from datetime import datetime

string_data_nascimento = input('Digite sua data de nascimento no formato dd/mm/yyyy: ')
data_nascimento_datetime = datetime.strptime(string_data_nascimento, '%d/%m/%Y')
data_atual = datetime.now()
idade = data_atual.year - data_nascimento_datetime.year

empregos = []
total_dias_trabalhados = 0
contador = 1

while True:
    string_admissao = input(f'Digite a data de admissão do seu {contador}° emprego no formato [dd/mm/yyyy]: ')
    string_demissao = input(f'Digite a data de demissão do seu {contador}° emprego no formato [dd/mm/yyyy]: ')
    admissao_datetime = datetime.strptime(string_admissao, '%d/%m/%Y')
    demissao_datetime = datetime.strptime(string_demissao, '%d/%m/%Y')
    dias_trabalhados = demissao_datetime - admissao_datetime
    empregos.append(dias_trabalhados)
    total_dias_trabalhados += int(dias_trabalhados.days)
    contador += 1
    continuar = str(input('Deseja inserir mais um emprego? [S/N]: ')).strip().upper()
    if continuar in 'Nn':
        break
print('~' * 30)
print(' RESUMO '.center(30, '-'))
print('~' * 30)
for k, v in enumerate(empregos):
    print(f'No seu {k + 1}° emprego você trabalhou {v.days} dias.')
print(f'Aos {idade} anos você trabalhou um total de {total_dias_trabalhados} dias.')
