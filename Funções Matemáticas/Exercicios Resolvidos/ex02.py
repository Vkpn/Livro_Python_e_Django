res = float(input('Qual o valor do resultado fiscal da empresa: '))
if res >= 0:
    print(f'Houve lucro de R${res:.2f}')
else:
    print(f'Houve prejuizo de R${abs(res):.2f}')
