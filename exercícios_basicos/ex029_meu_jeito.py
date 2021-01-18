from random import randint

cores = {
    'limpo':'\033[m',
    'vermelho':'\033[31m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
}

a = randint(0, 9)
b = randint(10, 19)
c = randint(20, 30)

if b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c
else:
    maior = a

if b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c
else:
    menor = a
    
linha_amarela = f'{cores["amarelo"]}-=-' * 10 + f'{cores["limpo"]}'

print(linha_amarela)
print(f'A ordem crescente é {cores["vermelho"]}{menor}{cores["limpo"]} e {cores["verde"]}{maior}{cores["limpo"]}.')
print(f'A ordem decrescente é {cores["verde"]}{maior}{cores["limpo"]} e {cores["vermelho"]}{menor}{cores["limpo"]}.')
print(linha_amarela)
print(f'O maior é {cores["verde"]}{maior}{cores["limpo"]}')
print(f'O menor é {cores["vermelho"]}{menor}{cores["limpo"]}')
print(linha_amarela)
