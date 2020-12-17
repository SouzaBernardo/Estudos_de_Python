# Forma de pagamente e condições para pagamento
print('PAGAMENTO!')
# Valor do produto
valor_produto = input('Valor do produto: R$').strip()
# Adiquirir a forma de pagamento
print('Formas de pagamento:')
print('[1] - à vista dinheiro/cheque: 10% de desconto')
print('[2] - à vista Cartão: 5% de desconto')
print('[3] - 3x ou mais no cartão: 20% de juros')
# Resposta
forma_pagamento = int(input('Qual a forma de pagamento (somente o número)?'))
# Realizar a forma de pagamento
if forma_pagamento == 1:
    # Informar opção escolhida
    print('Escolha 1!')
    print('À vista no dinheiro ou cheque')
    valor_produto = float(valor_produto) - (float(valor_produto) / 10)
    print(f'Nessa opção o produto sai por R${valor_produto}.')
    
elif forma_pagamento == 2:
    # Informar forma de pagamento
    print('Escolha 2!')
    print('À vista no cartão.')
    # Calcular produto com desconto
    valor_produto = float(valor_produto) - (float(valor_produto) * 5 / 100)
    # Resultado
    print(f'Nessa opção o produto sai por R${valor_produto}.')

elif forma_pagamento == 3:
    # Informa a opção
    print('Escolha 3!')
    print('No cartão parcelado.')
    
    # Calcular juros
    juros_produto_ = float(valor_produto) + (float(valor_produto) * 2 / 10)
    
    # Identificar meses parcelados
    meses_parcelados = input('Meses parcelados:').strip()
    
    # Calcular o valores parcelados
    valor_juros_mensal = juros_produto_ / float(meses_parcelados.split()[0])
    valor_produto_parcelado = float(valor_produto) / float(meses_parcelados.split()[0])
    produto_mensal_jurado = valor_produto_parcelado + valor_juros_mensal
    
    # Respostas
    print(f'Nessa opção o produto sai por R${valor_produto_parcelado:.2f} ao mês.')
    print(f'Este produto foi parcelado em {meses_parcelados} meses.')

else:
    # Caso não tenha escolha
    print('Você não escolheu uma opção...') 