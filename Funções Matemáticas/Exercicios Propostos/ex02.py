from math import ceil, pow
largura = float(input('Qual a largura da sala em metros: '))
comprimento = float(input('Qual o comprimento da sala em metros: '))
ceramica = float(input('Qual o tamanho em cm da cerâmica quadrada: '))

sala = largura * comprimento
peca = pow((ceramica/100), 2)
contador = 0

while sala >= peca * (contador+1):
    contador += 1

print(f'Para pavimentar a sala será necessário {ceil(contador)} peças de cerâmica.')
