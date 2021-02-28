# Saber se as 3 retas fazem um riangulo

from time import sleep

cores = {
    'limpo':'\033[m',
    'vermelho':'\033[31m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
}

reta1 = float(input('Comprimento da primeira reta:'))
reta2 = float(input('Comprimento da segunda reta:'))
reta3 = float(input('Comprimento da terceira reta:'))

if reta2 < reta1 and reta2 < reta3: 
    menor = reta2
elif reta3 < reta1 and reta3 < reta2:
    menor = reta3
else:
    menor = reta1

if reta2 > reta1 and reta2 > reta3:
    maior = reta2
elif reta3 > reta1 and reta3 > reta2:
    maior = reta3
else:
    maior = reta1

if reta2 < maior and reta2 > menor:
    medio = reta2
elif reta3 < maior and reta3 > menor:
    medio = reta3
else:
    medio = reta1

linha = f'{cores["amarelo"]}-=-' * 9 + f'{cores["limpo"]}'

print(linha)
print(f'A ordem crescente é:')
sleep(1)
print(f'> {cores["amarelo"]}{menor}{cores["limpo"]}.')
sleep(1)
print(f'> {cores["amarelo"]}{medio}{cores["limpo"]}.')
sleep(1)
print(f'> {cores["amarelo"]}{maior}{cores["limpo"]}.')
print(linha)

if menor + medio > maior:
    print(f'Elas {cores["verde"]}fazem{cores["limpo"]} um {cores["amarelo"]}triangulo!{cores["limpo"]}')
else:
    print(f'Elas {cores["vermelho"]}não{cores["limpo"]} fazem um {cores["amarelo"]}triangulo!{cores["limpo"]}')

print(linha)
