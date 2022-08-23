alt = float(input('Digite a altura: '))
lar = float(input('Digite a largura: '))
pro = float(input('Digite a profundidade: '))
volume = alt * lar * pro
print(f'O recipiente tem {volume * 1000:.0f} Litros ou seja {volume:.2f}m³.')
