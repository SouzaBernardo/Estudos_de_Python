# Usar Cores no Python
nome = 'Bernardo'
cores = {'Limpa':'\033[4;34m',
        'azul':'\033[34m',
        'amarelo':'\033[33m'} # Dicionário

print(f'Olá, \033[4;34m{nome}\033[m')
print('{}, {}'.format(cores['azul'], cores['amarelo']))
print(f'{cores["azul"]}, {cores["amarelo"]}')

