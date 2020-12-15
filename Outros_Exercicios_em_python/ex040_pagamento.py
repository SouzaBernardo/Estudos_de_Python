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
elif forma_pagamento == 2:
    print('Escolha 2!')
elif forma_pagamento == 3:
    print('Escolha 3!')
else:
    # Caso não tenha escolha
    print('Você não escolheu uma opção...') 