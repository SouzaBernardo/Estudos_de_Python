# Jogo de Adivinha
from random import randint
from time import sleep
num = randint(0, 5)
cores = {
    'limpo':'\033[m',
    'amarelo':'\033[33m',
    'verde':'\033[32m',
    'vermelho':'\033[31m',
}

linha_verde = f'{cores["verde"]}-=-' * 9 + f'{cores["limpo"]}'
linha_amarela = f'{cores["amarelo"]}-=-' * 9 + f'{cores["limpo"]}'

print(linha_amarela)
print('Escolhi um número de 0 até 5.')
print(linha_amarela)

pergunta = int(input(f'{cores["verde"]}Sabe qual é? '))

print(linha_amarela)
sleep(1)
print(f'{cores["amarelo"]}Processando...')
sleep(1)
print(f'Quase lá...{cores["limpo"]}')
sleep(1)
print(linha_amarela)

if pergunta == num:
    print(f'{cores["verde"]}Acertou!!!{cores["limpo"]}')
else:
    print(f'{cores["vermelho"]}Errou!!!')
    print(f'Tente novamente...')

print(linha_verde)
print(f'O número era {cores["verde"]}{num}{cores["limpo"]}')
print(linha_verde)
print('\033[31m__FIM__\033[m')
