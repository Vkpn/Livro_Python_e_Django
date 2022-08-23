from salvar import salvar_configuracoes
from ler import ler_configuracao

nome = str(input('Nome do proprietário: '))
num = str(input('Numero se série: '))
mac = str(input('Endereço MAC: '))

salvar_configuracoes(nome, num, mac)
ler_configuracao()
