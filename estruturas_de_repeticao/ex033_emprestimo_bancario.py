# Aprovar um empréstimo bancário

cores = {
    'limpo':'\033[m',
    'vermelho':'\033[31m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
}

linha_amarela = f'{cores["amarelo"]}-=' * 25 + f'{cores["limpo"]}'

print(linha_amarela)
valor_da_casa = float(input('Valor da casa que dejesa comprar: R$'))
print(linha_amarela)
valor_do_salario = float(input('valor do seu salário: R$'))
print(linha_amarela)
anos_a_pagar = int(input('Em quantos anos quer pagar a casa? '))
print(linha_amarela)

meses_do_ano = anos_a_pagar * 12
prestacao = valor_da_casa / meses_do_ano 
porcentagem_do_salario = (valor_do_salario * 30) / 100

if prestacao >= porcentagem_do_salario:
    print(f'O emprestimo {cores["vermelho"]}foi negado{cores["limpo"]}.') # Será liberada
    print(f'O valor da casa {cores["vermelho"]}ultrapassou os 30%{cores["limpo"]} do seu salário.')
    print(linha_amarela)
else:
    print(f'{cores["verde"]}TUDO CERTO{cores["limpo"]}!!!') 
    print(f'Emprestimo {cores["verde"]}Aceito{cores["limpo"]}!!!')
    print(f'O valor da casa é {cores["verde"]}R${valor_da_casa:.2f}{cores["limpo"]}.')
    print(f'Você vai paragar em {cores["verde"]}{anos_a_pagar} anos{cores["limpo"]}.')
    print(linha_amarela)
