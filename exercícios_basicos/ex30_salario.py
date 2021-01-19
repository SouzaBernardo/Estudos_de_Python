# Aumento de salário
cores = {
    'limpo':'\033[m',
    '':'\033[m',
    'amarelo':'\033[33m',
}
salario = float(input('Qual o seu salário? R$'))
print('------------------------------------')
print('Seu salário é R${:.2f}'.format(salario))

if (salario >= 1250):
    porcentagem_aumento = float(salario * 10) / 100
    novo_salario = float(salario + porcentagem_aumento)
    print('------------------------------------')
    print('Você teve um aumento de 10%, ele é R${:.2f}'.format(porcentagem_aumento))
    print('------------------------------------')
    print('Seu salário atual ficou R${:.2f}'.format(novo_salario))
    print('------------------------------------')
else: 
    porcentagem_aumento = float(salario * 15) / 100
    novo_salario = float(salario + porcentagem_aumento)
    print('------------------------------------')
    print('Você teve o aumento de R${:.2f}'.format(porcentagem_aumento))
    print('------------------------------------')
    print('Seu salário atual é: R${:.2f}'.format(novo_salario))
    print('------------------------------------')
print('^__FIM__^')