# Dizer qual número é maior ou menor
cores = {
    'limpo':'\033[m',
    'vermelho':'\033[31m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
    'azul':'\033[34m',
}
linha = f'{cores["amarelo"]}-=' * 10 + f'{cores["limpo"]}'

print(linha)
print('\033[31mVamos analisar dois números?!\033[m')
print('Primeiro eu preciso que você me diga quais são eles!')

pri_num = input('Primeiro número:')
seg_num = input('Segundo número:')


menor = pri_num
maior = pri_num

if seg_num != pri_num:

    if seg_num < pri_num:
        menor = seg_num
        print('O \033[31mprimeiro\033[m número é \033[31mmaior\033[m')
    else:
        maior = seg_num
        print('O \033[31msegundo\033[m número é \033[31mmaior\033[m')

    print(f'O número \033[34mmaior\033[m é \033[34m{maior}\033[m.')
    print(f'O  número \033[32mmenor\033[m é \033[32m{menor}\033[m.')
else:
    print('Os números \033[31msão iguais\033[m!')
