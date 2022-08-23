from math import pow, sqrt
x1 = int(input('Digite a coordenada do eixo X do primeiro ponto: '))
y1 = int(input('Digite a coordenada do eixo y do primeiro ponto: '))
z1 = int(input('Digite a coordenada do eixo z do primeiro ponto: '))

x2 = int(input('Digite a coordenada do eixo X do segundo ponto: '))
y2 = int(input('Digite a coordenada do eixo y do segundo ponto: '))
z2 = int(input('Digite a coordenada do eixo z do segundo ponto: '))

x3 = int(input('Digite a coordenada do eixo X do terceiro ponto: '))
y3 = int(input('Digite a coordenada do eixo y do terceiro ponto: '))
z3 = int(input('Digite a coordenada do eixo z do terceiro ponto: '))

lado1 = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2) + pow(z2 - z1, 2))
lado2 = sqrt(pow(x3 - x2, 2) + pow(y3 - y2, 2) + pow(z3 - z2, 2))
lado3 = sqrt(pow(x1 - x3, 2) + pow(y1 - y3, 2) + pow(z1 - z3, 2))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Com os pontos passados podemos formar um triangulo.')
else:
    print('Nao é possível formar um triangulo com os pontos informados.')
