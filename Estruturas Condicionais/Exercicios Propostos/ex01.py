num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))

med = [num1, num2, num3]

print(f'A media entre os números é: {sum(med) / 3:.1f}')

if num2 > num1 > num3 or num3 > num1 > num2:
    print(f'A mediana é: {num1}')
elif num1 > num2 > num3 or num3 > num2 > num1:
    print(f'A mediana é: {num2}')
else:
    print(f'A mediana é: {num3}')

# print(f'A mediana entre os números é {sorted(med)[1]}.')
