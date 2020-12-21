# Sortear número e dizer se é par ou impar
from random import randint
from time import sleep
from colorama import init
init()
# Sortea o número
numero = randint(1, 100)
print('\033[33m-=-' * 8)
print('\033[32mSorteando um número...')
print('\033[33m-=-' * 8)
sleep(1)
# Informa número sorteado
print(f'\033[mO número sorteado é \033[32m{numero}\033[m.')
print('\033[33m-=-' * 8)
sleep(1)
# Indicar que o PC está pensando
print('\033[32mANALISANDO...')
print('\033[33m-=-\033[m' * 8)
sleep(1)
# Identificar se é ou não par
if numero % 2 == 0:
    print('Este número é \033[32mpar!') # Para PAR
else:
    print('Este número é \033[32mimpar!') # Para IMPAR
# FIM
print('\033[33m-=-' * 8)
print('\033[31m_FIM_')
print('\033[33m-=-' * 8)
