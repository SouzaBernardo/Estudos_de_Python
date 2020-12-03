# Aprovar um empréstimo bancário

# Adquirir informações
valor_da_casa = str(input('Valor da casa que dejesa comprar: R$')).lower().strip()
valor_do_salario = str(input('valor do seu salário: R$')).lower().strip()
anos_a_pagar = str(input('Em quantos anos quer pagar a casa? ')).lower().strip()

# Caso as respostas tenham ',' ao invés de '.'
if valor_da_casa.count(',') or valor_do_salario.count(','):
    valor_da_casa = valor_da_casa.replace(',', '.')
    valor_do_salario = valor_do_salario.replace(',', '.')
    print(valor_da_casa)
    print(valor_do_salario)

# Converter valores para números
valor_da_casa = int(valor_da_casa * 2)
