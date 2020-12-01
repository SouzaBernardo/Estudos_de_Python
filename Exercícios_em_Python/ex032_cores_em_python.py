# Usar Cores no Python
import colorama
colorama.init()

nome = 'Bernardo'
a = 3
b = 5
cores = {
    'limpa':'\033[m',
    'azul':'\033[34m',
    'amarelo':'\033[33m',
    'preto_branco':'\033[7;30m'}

print(f'Olá!{cores["azul"]}{nome}')
print(f'Os valores são \033[32m{a}\033[m e \033[34m{b}\033[m')
print('\033[31m Olá, mundo ')
