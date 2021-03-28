# Aumento de salário
cores = {
    'limpo':'\033[m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
}

linha = f'{cores["amarelo"]}-=' * 18 + f'{cores["limpo"]}'

print(linha)
salario = float(input('Qual o seu salário? R$'))
print(f'{cores["verde"]}Seu salário é R${salario:.2f}{cores["limpo"]}')
print(linha)

if (salario >= 1250):
    porcentagem = '10%'
    porcentagem_aumento = float(salario * 10) / 100
    novo_salario = float(salario + porcentagem_aumento)
else:
    porcentagem = '15%'
    porcentagem_aumento = float(salario * 15) / 100
    novo_salario = float(salario + porcentagem_aumento)

print(f'Você teve um {cores["verde"]}aumento{cores["limpo"]} de {cores["verde"]}{porcentagem}{cores["limpo"]}, ele é {cores["verde"]}R${porcentagem_aumento:.2f}{cores["limpo"]}.')
print(linha)
print(f'Seu {cores["verde"]}novo salário{cores["limpo"]} ficou {cores["verde"]}R${novo_salario:.2f}{cores["limpo"]}.')
print(linha)