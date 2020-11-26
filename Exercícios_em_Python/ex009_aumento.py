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
