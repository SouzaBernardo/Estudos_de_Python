# Forma de pagamente e condições para pagamento
print('PAGAMENTO!')
# Valor do produto
valor_produto = input('Valor do produto: R$')
# Adiquirir a forma de pagamento
print('Formas de pagamento:')
print('[1] - à vista dinheiro/cheque: 10% de desconto')
print('[2] - à vista Cartão: 5% de desconto')
print('[3] - 3x ou mais no cartão: 20% de juros')
# Resposta
forma_pagamento = int(input('Qual a forma de pagamento (somente o número)?'))
# Realizar a forma de pagamento
if forma_pagamento == 1:
    print('Escolha 1!')
    valor_produto = float(valor_produto) - (float(valor_produto) / 10)
    print(f'Produto com 10% de desconto é R${valor_produto}.')
elif forma_pagamento == 2:
    print('Escolha 2!')
    valor_produto = float(valor_produto) - (float(valor_produto) * 5 / 100)
    print(f'Produto com 5% de desconto é R${valor_produto}.')
elif forma_pagamento == 3:
    print('Escolha 3!') # Informa a opção
    # Calcular juros
    juros_produto_ = float(valor_produto) + (float(valor_produto) * 2 / 10)
    # Identificar meses parcelados
    meses_parcelados = input('Meses parcelados:')
    meses_parcelados = int(meses_parcelados) # Transforma para int
    # Calcular o valores parcelados
    valor_juros_mensal = juros_produto_ / meses_parcelados
    valor_produto_parcelado = valor_produto / meses_parcelados
    produto_mensal_jurado = valor_produto_parcelado + valor_juros_mensal
    # Respostas
    print(f'O produto é R${valor_produto}.')
    print(f'Este produto foi parcelado em {meses_parcelados} meses')
    print(f'Valor mensal do produto (Com Juros): R${produto_mensal_jurado}')
else:
    # Caso não tenha escolha
    print('Você não escolheu uma opção...') 