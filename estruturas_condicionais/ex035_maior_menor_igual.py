# Dizer qual número é maior ou menor
cores = {
    'limpo': '\033[m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
}

linha = f'{cores["amarelo"]}-=' * 27 + f'{cores["limpo"]}'
opcoes = [f'{cores["vermelho"]}primeiro{cores["limpo"]}', f'{cores["verde"]}segundo{cores["limpo"]}',]

print(linha)
print('Vamos analisar dois números?!')
print(f'Primeiro eu preciso que você me diga quais são eles!')

print(linha + f'{cores["vermelho"]}')
pri_num = input('Primeiro número:')

print(linha + f'{cores["verde"]}')
seg_num = input('Segundo número:')

print(linha)

selecionado_menor = opcoes[0]
selecionado_maior = opcoes[0]
menor = pri_num
maior = pri_num

if seg_num != pri_num:
    if seg_num < pri_num:
        menor = seg_num
        selecionado_menor = opcoes[1]
    else:
        maior = seg_num
        selecionado_maior = opcoes[1]
else:
    print(f'Os números {cores["vermelho"]}SÃO IGUAIS{cores["limpo"]}!')

print(f'{selecionado_maior}({maior}) é {cores["azul"]}maior{cores["limpo"]}')
print(f'{selecionado_menor}({menor}) é {cores["azul"]}menor{cores["limpo"]}')