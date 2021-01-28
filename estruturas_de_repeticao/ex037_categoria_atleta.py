# Dizer a categoria de um atleta
cores = {
    'limpa':'\033[m',
    'azul':'\033[34m',
    'amarelo':'\033[33m',
    'verde':'\033[32m'
}# arrumar as cores
print('Vamos descobrir qual é sua categoria!')

idade_str = input('Qual a sua idade?').strip().lower() 
idade_int = int(idade_str.split()[0])

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

print(f'Devido a sua idade que é {idade_int} anos.')
