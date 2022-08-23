from datetime import datetime

sexo = str(input('Qual seu sexo? [M/F]: ')).strip().upper()
string_data_de_nascimento = str(input('Digite sua data de nascimento no formato dd/mm/yyyy: '))
data_de_nascimento_datetime = datetime.strptime(string_data_de_nascimento, '%d/%m/%Y')
data_atual = datetime.now()
idade = data_atual.year - data_de_nascimento_datetime.year
dias_para_aposentadoria_m = 365 * 35
dias_para_aposentadoria_f = 365 * 30
trabalhos = []
contador = 1

while True:
    string_admissao = str(input(f'Data de admissão no seu {contador}° emprego no formato [dd/mm/yyyy]: ')).strip()
    string_demissao = str(input(f'Data de demissão no seu {contador}° emprego no formato [dd/mm/yyyy]: ')).strip()
    admissao_datetime = datetime.strptime(string_admissao, '%d/%m/%Y')
    demissao_datetime = datetime.strptime(string_demissao, '%d/%m/%Y')
    dias_trabalhados = demissao_datetime - admissao_datetime
    trabalhos.append(dias_trabalhados.days)
    contador += 1
    continuar = str(input('Deseja inserir outro emprego? [S/N]: ')).strip().upper()
    if continuar in 'Nn':
        break
print('~' * 40)
print(' Aposentadoria '.center(40, '-'))
print('~' * 40)

anos = round(sum(trabalhos) / 365, 2)

if sexo in 'Mm':
    if idade >= 65 and sum(trabalhos) >= dias_para_aposentadoria_m:
        print(f'Com {idade} anos e {anos} anos trabalhados. Você já está apto a se aposentar.')
    elif idade >= 65 and sum(trabalhos) < dias_para_aposentadoria_m:
        print(f'Com {idade} anos e {anos} anos trabalhados. Faltam {round(35 - anos, 2)} anos de trabalho para se aposentar.')
    elif idade < 65 and sum(trabalhos) < dias_para_aposentadoria_m:
        print(f'Com {idade} anos e {anos} anos trabalhados. faltam {65 - idade} anos e {round(35 - anos, 2)} anos trabalhados para se aposentar.')
elif sexo in 'Ff':
    if idade >= 62 and sum(trabalhos) >= dias_para_aposentadoria_f:
        print(f'Com {idade} anos e {anos} anos trabalhados. Você já está apto a se aposentar.')
    elif idade >= 62 and sum(trabalhos) < dias_para_aposentadoria_f:
        print(f'Com {idade} anos e {anos} anos trabalhados. Faltam {round(30 - anos, 2)} anos de trabalho para se aposentar.')
    elif idade < 62 and sum(trabalhos) < dias_para_aposentadoria_f:
        print(f'Com {idade} anos e {anos} anos trabalhados. faltam {62 - idade} anos e {round(30 - anos, 2)} anos trabalhados para se aposentar.')
