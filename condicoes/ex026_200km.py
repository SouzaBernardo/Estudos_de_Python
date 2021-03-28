# Preço de uma viagem
from time import sleep

cores = {
    'limpo':'\033[m',
    'verde':'\033[32m',
    'amarelo':'\033[33m'
}
linha_verde = f'{cores["verde"]}-=-' * 11 + f'{cores["limpo"]}'

print(linha_verde)
print(f'{cores["amarelo"]}Preço da viagem...{cores["limpo"]}')
print(linha_verde)

km = str(input('Digite a distância de sua viagem: ')).strip()
km = float(km.split()[0])
print(linha_verde)

sleep(1)

print(f'{cores["amarelo"]}ANALISANDO...')
print(linha_verde)

sleep(1)

if km <= 200:
    preco = km * 0.5
else:
    preco = km * 0.45

print(f'Sua viagem vai custar: {cores["amarelo"]}R${preco:.2f}{cores["limpo"]}')
print(linha_verde)