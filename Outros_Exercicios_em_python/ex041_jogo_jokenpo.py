# Jogo de Pedra, papel e tesoura
from random import choice
from colorama import init
init()
# Opção do computador, assim ele vai escolher qual vai jogar
opcoes_computador = ['Pedra', 'Papel', 'Tesoura']
escolha_computador = choice(opcoes_computador)
# Pedir opção do jogador
print('O computador já fez sua escolha, só falta você!')
print('Opções:')
print('[1] - Pedra')
print('[2] - Papel')
print('[3] - Tesoura')
escolha_jogador = int(input('Qual dessas opções você escolhe (Somente o número)? '))
# Opção do jogador
if escolha_jogador == 1:
    escolha_jogador = 'Pedra'
elif escolha_jogador == 2:
    escolha_jogador = 'Papel'
else:
    escolha_jogador = 'Tesoura'
print(escolha_computador, escolha_jogador)
escolhas_dos_dois = [escolha_computador, escolha_jogador]

# Definir ganhador
if escolha_jogador != escolha_computador:
    if escolhas_dos_dois == ['Pedra', 'Papel']:
        print('Papel ganhou!')
        print('Quem ganhou foi o PC!')
    elif escolhas_dos_dois == ['Pedra', 'Tesoura']:
        print('Pedra ganhou!')
    else:
        print()
else:
    print('Empate')