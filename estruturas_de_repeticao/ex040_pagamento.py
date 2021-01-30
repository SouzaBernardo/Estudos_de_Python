# Forma de pagamente e condições para pagamento
from time import sleep
cores = {
    'limpo':'\033[m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
    'azul':'\033[34m',
}# arrumar as cores
print('PAGAMENTO!')
valor_produto = input('Valor do produto: R$').strip()

sleep(1)

print('Formas de pagamento:')
print('[1] - à vista dinheiro/cheque: 10% de desconto')
print('[2] - à vista Cartão: 5% de desconto')
print('[3] - 3x ou mais no cartão: 20% de juros')
sleep(1)

forma_pagamento = int(input('Qual a forma de pagamento (somente o número)?'))

if forma_pagamento == 1:
    print('Escolha 1!')
    print('À vista no dinheiro ou cheque')
    valor_produto = float(valor_produto) - (float(valor_produto) / 10)
    print(f'Nessa opção o produto sai por R${valor_produto}.')
    
elif forma_pagamento == 2:
    print('Escolha 2!')
    print('À vista no cartão.')
    valor_produto = float(valor_produto) - (float(valor_produto) * 5 / 100)
    print(f'Nessa opção o produto sai por R${valor_produto}.')

elif forma_pagamento == 3:
    print('Escolha 3!')
    print('No cartão parcelado.')
    juros_produto_ = float(valor_produto) + (float(valor_produto) * 2 / 10)
    meses_parcelados = input('Meses parcelados:').strip()

    valor_juros_mensal = juros_produto_ / float(meses_parcelados.split()[0])
    valor_produto_parcelado = float(valor_produto) / float(meses_parcelados.split()[0])
    produto_mensal_jurado = valor_produto_parcelado + valor_juros_mensal
    print(f'Nessa opção o produto sai por R${valor_produto_parcelado:.2f} ao mês.')
    print(f'Este produto foi parcelado em {meses_parcelados} meses.')

else:
    print('Você não escolheu uma opção...')  # fazer com que isso venha antes