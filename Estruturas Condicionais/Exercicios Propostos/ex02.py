l1 = float(input('Digite a medida do primeiro lado: '))
l2 = float(input('Digite a medida do segundo lado: '))
l3 = float(input('Digite a medida do terceiro lado: '))

hip = 0
co = 0
ca = 0

if l1 > l2 and l1 > l3:
    hip = l1
    co = l2
    ca = l3
elif l2 > l1 and l2 > l3:
    hip = l2
    co = l1
    ca = l3
elif l3 > l1 and l3 > l2:
    hip = l3
    co = l2
    ca = l1

if hip**2 == (co**2 + ca**2):
    print('Podemos formar um triangulo retângulo!')
else:
    print('Não podemos formar um triangulo retângulo.')
