# Dizer o aumento do salário

# Pedir salário
salario = str(input('Olá, qual seu salário atual?')).upper().strip()
# Pedir a porcentagem de aumento
aumento = str(input('E qual a porcentagem para o aumento?')).upper().strip()
# Desconsiderar R$ e REAIS no salário
if salario.count('REAIS'):
    salario = salario.replace('REAIS', '')
if salario.count('R$'):
    salario = salario.replace('R$', '')
# Desconsiderar % e PORCENTO
if aumento.count('PORCENTO'):
    aumento = aumento.replace('PORCENTO', '')
if aumento.count('%'):
    aumento = aumento.replace('%', '')
# Tornar variáveis em float
salario = float(salario)
aumento = float(aumento)
# Calcular a porcentagem do aumento
calcular_aumento = salario * aumento / 100
juntar_aumento_salario = calcular_aumento + salario
# Dar resultado
print(f'Antigamente seu salário era R${salario}')
print(f'E, você recebeu um aumento de {aumento}%')
print(f'O aumento do seu salário ficou {juntar_aumento_salario}')
print('__FIM__')
