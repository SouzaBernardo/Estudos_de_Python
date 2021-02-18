# Forma de pagamente e condições para pagamento
# from time import sleep
cores = {
    'limpo':'\033[m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
    'azul':'\033[34m',
}# arrumar as cores

linha = f'{cores["amarelo"]}-=' * 30 + f'{cores["limpo"]}'
opcoes_de_pagamento = ['à vista dinheiro/cheque: 10% de desconto', 'à vista Cartão: 5% de desconto.', '3x ou mais no cartão: 20% de juros']

print(linha)

print('PAGAMENTO!')
valor_produto = input('Valor do produto: R$').strip()

print(linha)

print('Formas de pagamento:')
print(f'[1] - {opcoes_de_pagamento[0]}')
print(f'[2] - {opcoes_de_pagamento[1]}')
print(f'[3] - {opcoes_de_pagamento[2]}')
forma_pagamento = int(input('Qual a forma de pagamento (somente o número)?'))

if forma_pagamento < 1 or forma_pagamento > 3:
    print('Você não escolheu uma opção...')
else:
    if forma_pagamento == 1:
        escolha = '1'
        opcoes_de_pagamento = opcoes_de_pagamento[0]

        valor_produto = float(valor_produto) - (float(valor_produto) / 10)
        print(f'Nessa opção o produto sai por R${valor_produto}.') # valor
        
    elif forma_pagamento == 2:
        escolha = '2'
        opcoes_de_pagamento = opcoes_de_pagamento[1]

        valor_produto = float(valor_produto) - (float(valor_produto) * 5 / 100) # valor
        print(f'Nessa opção o produto sai por R${valor_produto}.')

    else:
        escolha = '3'
        opcoes_de_pagamento = opcoes_de_pagamento[2]

        valor_produto = float(valor_produto) + (float(valor_produto) * 2 / 10)

        meses_parcelados = input('Meses parcelados:').strip()
        if float(meses_parcelados[0]) < 3: # arrumar aqui
            print('Erro! Deve ser acima de 3 meses!')
        else: # reparar daqui para baixo...
            valor_juros_mensal = valor_produto / float(meses_parcelados.split()[0])
            valor_produto_parcelado = float(valor_produto) / float(meses_parcelados.split()[0])
            produto_mensal_jurado = valor_produto_parcelado + valor_juros_mensal

        print(f'Nessa opção o produto sai por R${valor_produto_parcelado:.2f} ao mês.')
        print(f'Este produto foi parcelado em {meses_parcelados} meses.')

print(f'Escolha {escolha}!')
print(f'Forma de pagamento: {opcoes_de_pagamento}')
print(f'Nesta forma o produto sai por: R${valor_produto}')
