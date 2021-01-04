salario = float(input('Qual o seu salário? R$')) # pede o salário
print('------------------------------------')
print('Seu salário é R${:.2f}'.format(salario)) # indica o salario

if (salario >= 1250): # se for maior ou igual a 1250 
    porcentagem_aumento = float(salario * 10) / 100 # calcula o aumento
    novo_salario = float(salario + porcentagem_aumento) # novo salario
    print('------------------------------------')
    # indica a porcentagem do salário
    print('Você teve um aumento de 10%, ele é R${:.2f}'.format(porcentagem_aumento))
    print('------------------------------------')
    # indica o novo salário
    print('Seu salário atual ficou R${:.2f}'.format(novo_salario))
    print('------------------------------------')
else: 
    porcentagem_aumento = float(salario * 15) / 100 # calcula o aumento
    novo_salario = float(salario + porcentagem_aumento) # novo salario
    print('------------------------------------')
    # indica a porcentagem do salário
    print('Você teve o aumento de R${:.2f}'.format(porcentagem_aumento))
    print('------------------------------------')
    # indica o novo salário
    print('Seu salário atual é: R${:.2f}'.format(novo_salario))
    print('------------------------------------')
print('^__FIM__^')