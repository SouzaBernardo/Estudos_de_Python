# Aprendendo usar Cores no Python

'''Tipos de cor:
    0 → Sem style
    1 → Negrito**
    4 → Underline
    7 → Inverte
    ------------------
    30 - Branco
    31 - Vermelho
    32 - Verde
    33 - Amarelo
    34 - Azul
    35 - Violeta
    36 - Ciano
    37 - Cinza'''

nome = 'Bernardo'
a = 3
b = 5
cores = {
    'limpa':'\033[m',
    'azul':'\033[34m',
    'amarelo':'\033[33m',
    'verde':'\033[32m'
}

print(f'Olá!{cores["azul"]}{nome}')
print(f'Os valores são {cores["verde"]}{a}{cores["limpa"]} e {cores["verde"]}{b}{cores["limpa"]}')
