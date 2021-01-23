# Escolher um número e se que ele em Binário, Octal ou Hexadecimal

from time import sleep

cores = {
    'limpo':'\033[m',
    'vermelho':'\033[31m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
}

linha = f'{cores["amarelo"]}-=' * 30 + f'{cores["limpo"]}'

print(linha)
print(f'{cores["verde"]}Olá! Escolha um {cores["amarelo"]}número inteiro{cores["verde"]} e vamos converter suas bases.{cores["amarelo"]}')
numero_escolhido = int(input('Digite o número:'))
print(linha)
print('Escolha a base que você quer converter...')
print('[1] - Binário')
print('[2] - Octal')
print('[3] - Hexadecimal')
print(linha)
escolha_da_base = int(input('Qual base que deseja?'))
sleep(1)
print(linha)
print(f'{cores["verde"]}ANALISANDO...{cores["limpo"]}')
print(linha)
sleep(1)
if escolha_da_base > 3:
    print(f'{cores["vermelho"]}Este número não é válido! TENTE DE NOVO!{cores["limpo"]}')
else:
    if escolha_da_base == 1:
        numero_escolhido_convertido = bin(numero_escolhido)
        print(f'{cores["verde"]}Convertemos seu número para {cores["amarelo"]}BINÁRIO{cores["limpo"]}!')
        print(f'Seu número ({cores["verde"]}{numero_escolhido}{cores["limpo"]}) em binário é {cores["verde"]}{numero_escolhido_convertido}{cores["limpo"]}.')
    elif escolha_da_base == 2:
        numero_escolhido_convertido = oct(numero_escolhido)
        print(f'{cores["verde"]}Convertemos seu número para {cores["amarelo"]}OCTAL{cores["limpo"]}!')
        print(f'Seu número ({cores["verde"]}{numero_escolhido}{cores["limpo"]}) em octal é {cores["verde"]}{numero_escolhido_convertido}{cores["limpo"]}.')
    else:
        numero_escolhido_convertido = hex(numero_escolhido)
        print(f'{cores["verde"]}Convertemos seu número para {cores["amarelo"]}Hexadecimal{cores["limpo"]}!')
        print(f'Seu número ({cores["verde"]}{numero_escolhido}{cores["limpo"]}) em Hexadecimal é {cores["verde"]}{numero_escolhido_convertido}{cores["limpo"]}.')
print(linha)
