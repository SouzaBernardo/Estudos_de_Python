# Dizer a categoria de um atleta
cores = {
    'limpo':'\033[m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
}

linha = f'{cores["amarelo"]}-=' * 30 + f'{cores["limpo"]}'

print(linha)
print('Vamos descobrir qual é sua categoria!')
print(linha)

idade_str = input('Qual a sua idade?').strip().lower() 
idade_int = int(idade_str.split()[0])

print(linha)

if idade_int <= 9:
    categoria = 'MIRIM'
elif idade_int <= 14:
    categoria = 'INFATIL'
elif idade_int <= 19:
    categoria = 'JÚNIOR'
elif idade_int <= 20:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'

print(f'Sua categoria é {cores["verde"]}{categoria}{cores["limpo"]}')
print(f'Devido a sua idade que é {cores["verde"]}{idade_int} anos{cores["limpo"]}.')
print(linha)
