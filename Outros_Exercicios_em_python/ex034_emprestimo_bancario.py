# Aprovar um empréstimo bancário
from colorama import init
init()

# Adquirir informações
valor_da_casa = str(input('Valor da casa que dejesa comprar: R$')).lower().strip()
valor_do_salario = str(input('valor do seu salário: R$')).lower().strip()
anos_a_pagar = str(input('Em quantos anos quer pagar a casa? ')).lower().strip()

# 
if valor_da_casa.count(',') or valor_do_salario.count(','):
    print('\033[31m ERRO!')
    print('Você usou virgula! ao invés disso, use ponto.')
elif valor_da_casa.count('.') or valor_do_salario.count('.'):
    # Converter valores para números
    valor_da_casa = float(valor_da_casa)
    valor_do_salario = float(valor_do_salario)
elif anos_a_pagar.count('.'):
    anos_a_pagar = float(anos_a_pagar)
else: 
    print('')
print(valor_da_casa, valor_do_salario, anos_a_pagar)