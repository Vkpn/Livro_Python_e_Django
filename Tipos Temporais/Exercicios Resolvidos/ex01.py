from datetime import datetime
nascimento = input('Data de nascimento no modelo [dd/mm/yyyy]: ')
data_nascimento = datetime.strptime(nascimento, '%d/%m/%Y')
data_atual = datetime.now()
dif = data_atual - data_nascimento
print(f'De {data_nascimento.strftime("%d/%m/%Y")} até {data_atual.strftime("%d/%m/%Y")} a pessoa viveu {dif.days} dias.')
