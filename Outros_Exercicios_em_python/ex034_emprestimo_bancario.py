# Aprovar um empréstimo bancário
from colorama import init
init()

# Adquirir informações
valor_da_casa = str(input('Valor da casa que dejesa comprar: R$')).lower().strip()
valor_do_salario = str(input('valor do seu salário: R$')).lower().strip()
anos_a_pagar = str(input('Em quantos anos quer pagar a casa? ')).lower().strip()

# Converter para numero, int ou float

if valor_da_casa.count(',') or valor_do_salario.count(',') or anos_a_pagar.count(','):
    # ERRO
    print('\033[31mERRO!')
    print('\033[31mNÃO USE VIRGULA\033[m, MAS SIM \033[31mPONTO!\033[m.')

elif valor_do_salario.count('.') or valor_da_casa.count('.') or anos_a_pagar.count('.'):
    # Caso tenha .
    if valor_do_salario.count('.') and valor_da_casa.count('.') and anos_a_pagar.count('.'):
        valor_da_casa = float(valor_da_casa)
        valor_do_salario = float(valor_do_salario)
        anos_a_pagar = float(anos_a_pagar)        
    elif valor_do_salario.count('.') and valor_da_casa.count('.'):
        valor_da_casa = float(valor_da_casa)
        valor_do_salario = float(valor_do_salario)
        anos_a_pagar = int(anos_a_pagar)
    elif valor_do_salario.count('.') and anos_a_pagar.count('.'):
        valor_da_casa = int(valor_da_casa)
        valor_do_salario = float(valor_do_salario)
        anos_a_pagar = float(anos_a_pagar)
    else:
        valor_da_casa = float(valor_da_casa)
        valor_do_salario = int(valor_do_salario)
        anos_a_pagar = float(anos_a_pagar)      
else:
    valor_da_casa = int(valor_da_casa)
    valor_do_salario = int(valor_do_salario)
    anos_a_pagar = int(anos_a_pagar)

# Calcular
valor_por_mes_casa = anos_a_pagar * 12 # Quantos meses vai pagar
porcentagem_do_salario = (valor_do_salario * 30) / 100 # Porcentagem

# Ver se pode ou não comprar a casa
if valor_por_mes_casa >= porcentagem_do_salario:
    print('Você \033[31mnão pode comprar\033[m a casa, \033[31multrapassou os 30%\033[m.')
else:
    print('\033[32m TUDO CERTO.\033[m')
    print('Você pode comprar a casa!')
    print(f'O valor dela é \033[32m R${valor_da_casa}\033[m e você vai paragar em \033[32m {valor_por_mes_casa} meses\033[m.')
