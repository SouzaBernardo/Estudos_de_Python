# Sortear número e dizer se é par ou impar
from random import randint
from time import sleep

numero = randint(1, 100)

cores = {
    'limpo':'\033[m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
}
linha_amarela = f'{cores["amarelo"]}-=-' * 8 + f'{cores["limpo"]}'

print(linha_amarela)
print(f'{cores["verde"]}Sorteando um número...')
print(linha_amarela)
sleep(1)
print(f'{cores["limpo"]}Ele é {cores["verde"]}{numero}{cores["limpo"]}.')
print(linha_amarela)
sleep(1)
print(f'{cores["verde"]}ANALISANDO...{cores["limpo"]}')
print(linha_amarela)
sleep(1)

if numero % 2 == 0:
    print(f'Este número é {cores["verde"]}par!{cores["limpo"]}')
else:
    print(f'Este número é {cores["verde"]}impar!{cores["limpo"]}')

print(linha_amarela)
