# Identificar ano bissexto
cores = {
    'limpo':'\033[m',
    'amarelo':'\033[33m',
    'verde':'\033[32m',
    'vermelho':'\033[31m',
}

linha_amarela = f'{cores["amarelo"]}-=-' * 8 + f'{cores["limpo"]}'

print(linha_amarela)
ano = int(input('Qual ano que você está? '))
print(linha_amarela)

if ano % 4 == 0:
    print(f'Você {cores["verde"]}está{cores["limpo"]} em um ano {cores["amarelo"]}bissexto{cores["limpo"]}.')
else:
    print(f'Você {cores["vermelho"]}não{cores["limpo"]} está em um ano {cores["amarelo"]}bissexto{cores["limpo"]}.')

print(linha_amarela)
