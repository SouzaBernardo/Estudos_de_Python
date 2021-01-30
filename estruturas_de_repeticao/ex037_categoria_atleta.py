# Dizer a categoria de um atleta
cores = {
    'limpo':'\033[m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
    'azul':'\033[34m',
}

linha = f'{cores["amarelo"]}-=' * 30 + f'{cores["limpo"]}'

print(linha)
print('Vamos descobrir qual é sua categoria!')
print(linha)

idade_str = input('Qual a sua idade?').strip().lower() 
idade_int = int(idade_str.split()[0])

print(linha)

if idade_int <= 9:
    print('Sua categoria é MIRIM!')
elif idade_int <= 14:
    print('Sua categoria é INFATIL')
elif idade_int <= 19:
    print('Sua categoria é JÚNIOR')
elif idade_int <= 20:
    print('Sua categoria é SÊNIOR')
else:
    print('Sua categoria é MASTER')
print(f'Devido a sua idade que é {cores["verde"]}{idade_int}{cores["limpo"]} anos.')
print(linha)
