# Usar Cores no Python
import colorama
colorama.init()

nome = 'Bernardo'
cores = {'Limpa':'\033[0;30m',
        'azul':'\033[34m',
        'amarelo':'\033[33m'} # Dicionário

print(f'Olá, \033[4;32m{nome}\033[m')
print('{}, {},'.format(cores['azul'], cores['amarelo']))
print(f'{cores["azul"]}, {cores["amarelo"]}')

