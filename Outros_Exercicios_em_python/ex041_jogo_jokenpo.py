# Jogo de Pedra, papel e tesoura
from random import randint
from time import sleep
from colorama import init
init() # Colors

# Opção do computador, assim ele vai escolher qual vai jogar

opcoes = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2) # escolhe de 0 a 2 para dentro das opções

# Pedir opção do jogador

print('O computador já fez sua escolha, só falta você!')
print('Opções:')
print('[1]- \033[1;44mPedra\033[m ')
print('[2] - \033[1;45mPapel\033[m')
print('[3] - \033[1;46mTesoura\033[m')

jogador = int(input('Qual a sua jogada? '))

sleep(1)
print('\033[1;44m Pedra \033[m')
sleep(1)
print('\033[1;45m Papel \033[m')
sleep(1)
print('\033[1;46m Tesoura \033[m')
sleep(1)

print('-=' * 11)
print(f'Computador jogou {opcoes[computador]}')
print(f'Jogador jogou {opcoes[jogador - 1]}') # pega na lista de opções as alternativas
print('-=' * 11)

# Resultado
if computador != (jogador - 1):
    if computador == 0: # Pedra 
        if (jogador - 1) == 1: # Papel
            print('Jogador ganhou')
        elif (jogador - 1) == 2: # Tesoura
            print('Computador Ganhou')
    elif computador == 1: # Papel
        if (jogador - 1) == 0: # Pedra 
            print('Computador Ganhou')
        elif (jogador - 1) == 2: # Tesoura
            print('Jogador Ganhou')
    elif computador == 2: # Tesoura
        if (jogador - 1) == 0: # Pedra 
            print('Jogador Ganhou')
        elif (jogador - 1) == 1: # Papel 
            print('Computador Ganhou')
else:
    print('Empate!')
print('\033[31m__FIM__\033[m')