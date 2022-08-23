sala = [float(input('Digite a largura da sala em metros: ')),
        float(input('Digite o comprimento da sala em metros: '))]

ceramica = [float(input('Digite o tamanho da peça quadrada de cerâmica em centímetros: ')),
            float(input('Digite o valor da peça de cerâmica: '))]

tamanho_sala = sala[0] * sala[1]
quantidade_de_pecas = tamanho_sala / (ceramica[0] / 100)
valor = quantidade_de_pecas * ceramica[1]

print(
    f'A sala tem {tamanho_sala:.2f}m³\nSerá necessário {quantidade_de_pecas:.0f} peças de cerâmica\nValor total da obra é R$ {valor:.2f}')
