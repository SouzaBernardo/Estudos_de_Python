# Aprovar um empréstimo bancário

from colorama import init
init()

# Adquirir informações

valor_da_casa = str(input('Valor da casa que dejesa comprar: R$'))
valor_do_salario = str(input('valor do seu salário: R$'))
anos_a_pagar = str(input('Em quantos anos quer pagar a casa? '))

# Converter para INT, FLOAT ou dar ERRO

if valor_da_casa.count(',') or valor_do_salario.count(',') or anos_a_pagar.count(','):
    # Indicar erro se houver virgula
    print('\033[31mERRO!\033[m.')
    print('Você usou \033[31mvirgula\033[m. Tente usar \033[31mPonto\033[m!')

elif anos_a_pagar.count('.'):
    # Indicar erro se tiver ano quebrado
    print('\033[31mERRO!\033[m.')
    print('Você usou \033[31m"."\033[m na \033[31m3° opção\033[m.')
    print('Use \033[31mnúmeros inteiros nessa opção\033[m.')
    print('Tente novamente!') # tente novamente 

elif valor_da_casa.count('.') and valor_do_salario.count('.'):
    # Caso a casa e o salario tenha '.'
    valor_da_casa = float(valor_da_casa)
    valor_do_salario = float(valor_do_salario)
    anos_a_pagar = int(anos_a_pagar)

elif valor_da_casa.count('.'):
    # Caso só a casa tenha '.'
    valor_da_casa = float(valor_da_casa)
    valor_do_salario = int(valor_do_salario)
    anos_a_pagar = int(anos_a_pagar)

elif valor_do_salario.count('.'):
    # Caso o salário tenha '.'
    valor_da_casa = int(valor_da_casa)
    valor_do_salario = float(valor_do_salario)
    anos_a_pagar = int(anos_a_pagar)

else:
    # Caso nada tenha ponto, transformar para int
    valor_da_casa = int(valor_da_casa)
    valor_do_salario = int(valor_do_salario)
    anos_a_pagar = int(anos_a_pagar)

# Calcular o resultado

meses_do_ano = anos_a_pagar * 12 # Quantos meses até concluir o pagamento
prestacao = valor_da_casa / meses_do_ano # Quanto se pagara por mês
porcentagem_do_salario = (valor_do_salario * 30) / 100 # Porcentagem do salário

# Analisar se o emprestimo será liberado
if prestacao >= porcentagem_do_salario:
    # Não será liberado
    print('O emprestimo \033[31mfoi negado\033[m.') # Será liberada
    print('O valor da casa \033[31multrapassou os 30%\033[m do seu salário.')
else:
    # Será liberada
    print('\033[32m TUDO CERTO.\033[m') 
    print('Emprestimo \033[32mAceito\033[m')
    print(f'O valor da casa é \033[32mR${valor_da_casa}\033[m.')
    print(f'Você vai paragar em \033[32m{prestacao:.2f} meses\033[m.')
