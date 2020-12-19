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
print('[0] - Pedra')
print('[1] - Papel')
print('[2] - Tesoura')

jogador = int(input('Qual a sua jogada? '))

sleep(1)
print('Pedra')
sleep(1)
print('Papel')
sleep(1)
print('Tesoura')
sleep(2)

print('-=' * 11)
print(f'Computador jogou {opcoes[computador]}')
print(f'Jogador jogou {opcoes[jogador]}') # pega na lista de opções as alternativas
print('-=' * 11)

# Resultado
if computador == 0: # Pedra 
    if jogador == 0: # Pedra
        print('Empate!')
    elif jogador == 1: # Papel
        print('Jogador ganhou')
    elif jogador == 2: # Tesoura
        print('Computador Ganhou')
    else:
        print('Jogada inválida')
elif computador == 1: # Papel
    if jogador == 0: # Pedra 
        print('Computador Ganhou')
    elif jogador == 1: # Papel
        print('Empate')
    elif jogador == 2: # Tesoura
        print('Jogador Ganhou')
    else:
        print('Jogada inválida')
elif computador == 2: # Tesoura
    if jogador == 0: # Pedra 
        print('Jogador Ganhou')
    elif jogador == 1: # Papel 
        print('Computador Ganhou')
    elif jogador == 2: # Tesoura
        print('Empate')
    else:
        print('Jogada inválida')
print('__FIM__')