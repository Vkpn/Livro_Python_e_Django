num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print(f'O número {num1} é maior que o numero {num2}.')
elif num2 > num1:
    print(f'O número {num2} é maior que o numero {num1}.')
else:
    print(f'Os números são iguais.')
