num = []
for n in range(0, 5):
    num.append(int(input(f'Digite o {n+1} numero: ')))
print(sorted(num, reverse=True))
