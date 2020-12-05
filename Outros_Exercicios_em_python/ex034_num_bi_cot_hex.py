# Escolher um número e se que ele em Binário, Octal ou Hexadecimal
from colorama import init # importar cores
init()
print('\033[32mOlá! Escolha um número inteiro e vamos converter suas bases.\033[m')
# Pedir o número
numero_escolhido = int(input('Digite o número:'))
# Dar opções
print('Escolha a base que você quer converter...')
print('[1] - Binário')
print('[2] - Octal')
print('[3] - Hexadecimal')
# Pedir escolha
escolha_da_base = int(input('Qual base que deseja?'))
# Converter para as bases
if escolha_da_base == 1:
    # Converter para binário
    numero_escolhido_convertido = bin(numero_escolhido)
    print('\033[32mANALISANDO...\033[m')
    print('Convertemos seu número para \033[32mBINÁRIO\033[m!')
    print(f'Seu número ({numero_escolhido}) em binário é \033[32m{numero_escolhido_convertido}\033[m.')
elif escolha_da_base == 2:
    # Converter para octal
    numero_escolhido_convertido = oct(numero_escolhido)
    print('\033[32mANALISANDO...\033[m')
    print('Convertemos seu número para \033[32mOCTAL\033[m!')
    print(f'Seu número ({numero_escolhido}) em octal é \033[32m{numero_escolhido_convertido}\033[m.')
else:
    # Converter para Hexadecimal
    numero_escolhido_convertido = hex(numero_escolhido)
    print('\033[32mANALISANDO...\033[m')
    print('Convertemos seu número para \033[32mHexadecimal\033[m!')
    print(f'Seu número ({numero_escolhido}) em Hexadecimal é \033[32m{numero_escolhido_convertido}\033[m.')
print('\033[31m__FIM__\033[m')