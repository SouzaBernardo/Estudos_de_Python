# Jogo de Adivinha
from random import randint
from colorama import init
from time import sleep
init()
# Número entre 0 e 5
num = randint(0, 5)
# Dar o desafio
print('\033[33m-=-\033[m' * 9)
print('Escolhi um número de 0 à 5.')
print('\033[33m-=-\033[m' * 9)
# Resposta do usuário
pergunta = int(input(('Sabe qual é?')))
# Tempo...
print('\033[33mProcessando...')
sleep(2)
print('Quase lá...\033[m')
sleep(2)
# Condições
print('\033[32m-=-\033[m' * 9)
if pergunta == num: # caso ganhe
    print('\033[32mAcertou!!!\033[m') # Se acertar o número
else: # Caso erre
    print('\033[31mErrou!!!\033[m Tente novamente...') # Se errar o número
# Resultado
print('\033[32m-=-\033[m' * 9)
print(f'O número era \033[32m{num}\033[m') # Informa qual era o número
print('\033[32m-=-\033[m' * 9)
print('\033[31m__FIM__\033[m')
